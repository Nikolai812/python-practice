from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder

from dataclasses import dataclass
from configparser import ConfigParser


@dataclass
class FTSConfig:
    fts_input: list[str]
    fts_classified: list[str]
    fwhm: float
    low_threshold: float
    high_threshold: float
    dry_run: bool


def read_config(filename="fts_config.ini") -> FTSConfig:
    parser = ConfigParser()
    parser.read(filename)

    cfg = parser["DEFAULT"]

    return FTSConfig(
        fts_input=[
            s.strip()
            for s in cfg.get("fts_input", "").split(",")
            if s.strip()
        ],
        fts_classified=[
            s.strip()
            for s in cfg.get("fts_classified", "").split(",")
            if s.strip()
        ],
        fwhm=cfg.getfloat("fwhm", 3.0),
        low_threshold=cfg.getfloat("low_threshold", 5.0),
        high_threshold=cfg.getfloat("high_threshold", 10.0),
        dry_run=cfg.getboolean("dry_run", True),
    )



def get_star_sources(
    fits_image_path: str,
    fwhm: float = 3.0,
    threshold_factor: float = 5.0
):
    """
    Detect star-like sources in a FITS image.

    Parameters
    ----------
    fits_image_path : str
        Path to the FITS (.fts/.fits) image.
    fwhm : float, optional
        Approximate full width at half maximum of stars in pixels.
    threshold_factor : float, optional
        Detection threshold in units of background sigma.

    Returns
    -------
    astropy.table.Table or None
        Table of detected sources.
    """
    data = fits.getdata(fits_image_path)

    mean, median, std = sigma_clipped_stats(data)

    daofind = DAOStarFinder(
        fwhm=fwhm,
        threshold=threshold_factor * std
    )

    sources = daofind(data - median)

    return sources


if __name__ == "__main__":
    import os

    # The lists below collect the .fts file names with zero number of stars for threshold_factor=5,
    # zero number of stars for threshold_factor=10, but non_zero for threshold_factor=5,
    # non_zero number of stars woth
    zero_stars_th5 = []
    zero_stars_only_th10 = []
    non_zero_stars = []

    fts_dir = "FTS"  # Directory containing .fts files
    fwhm=3.0
    threshold_factor=5.0 # typical default -5
    for filename in os.listdir(fts_dir):
        if filename.endswith(".fts"):
            fts_file = os.path.join(fts_dir, filename)
            print("")
            print("####################################")
            print(fts_file)

            threshold_factor = 5.0
            sources_5th = get_star_sources(
                fits_image_path=fts_file,
                fwhm=fwhm,
                threshold_factor=threshold_factor
            )

            threshold_factor = 10.0
            sources_10th = get_star_sources(
                fits_image_path=fts_file,
                fwhm=fwhm,
                threshold_factor=threshold_factor
            )

            num_stars_5th = 0 if sources_5th is None else len(sources_5th)
            print(f"Detected {num_stars_5th} stars for threshold: {threshold_factor}, fwhm: {fwhm}")

            num_stars_10th = 0 if sources_10th is None else len(sources_10th)
            print(f"Detected {num_stars_10th} stars for threshold: {threshold_factor}")

            if num_stars_10th > 0:
                non_zero_stars.append(fts_file)
            elif num_stars_5th > 0:
                zero_stars_only_th10.append(fts_file)
                df = sources_5th.to_pandas()
                brightest = df.sort_values("flux", ascending=False)
                print(brightest.head(10))
            else:
                zero_stars_th5.append(fts_file)

            print("####################################")

        print("non zero stars:", non_zero_stars)
        print("zero stars only th10:", zero_stars_only_th10)
        print("zero stars th5:", zero_stars_th5)