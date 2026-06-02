from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder


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
    # import pandas as pd

    fts_dir = "FTS"  # Directory containing .fts files
    fwhm=3.0
    threshold_factor=5.0 # typical default -5
    for filename in os.listdir(fts_dir):
        if filename.endswith(".fts"):
            fts_file = os.path.join(fts_dir, filename)
            print("")
            print("####################################")
            print(fts_file)
            sources = get_star_sources(
                fits_image_path=fts_file,
                fwhm=fwhm,
                threshold_factor=threshold_factor
            )



            num_stars = 0 if sources is None else len(sources)
            print(f"Detected {num_stars} stars")

            if num_stars > 0:
                df = sources.to_pandas()
                brightest = df.sort_values("flux", ascending=False)
                print(brightest.head(10))

            print("####################################")

