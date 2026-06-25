from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder

from dataclasses import dataclass
from configparser import ConfigParser
from pathlib import Path


@dataclass
class FTSConfig:
    fts_input: list[str]
    fts_classified: list[str]
    fwhm: float
    low_threshold: float
    high_threshold: float
    dry_run: bool


def read_config(filename: str = "fts_config.ini") -> FTSConfig:
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
    threshold_factor: float = 5.0,
):
    data = fits.getdata(fits_image_path)

    mean, median, std = sigma_clipped_stats(data)

    daofind = DAOStarFinder(
        fwhm=fwhm,
        threshold=threshold_factor * std,
    )

    return daofind(data - median)


def process_fts_file(
    fts_file: Path,
    config: FTSConfig,
    zero_stars_th5: list[str],
    zero_stars_only_th10: list[str],
    non_zero_stars: list[str],
) -> None:

    print()
    print("####################################")
    print(fts_file)

    sources_low = get_star_sources(
        fits_image_path=str(fts_file),
        fwhm=config.fwhm,
        threshold_factor=config.low_threshold,
    )

    sources_high = get_star_sources(
        fits_image_path=str(fts_file),
        fwhm=config.fwhm,
        threshold_factor=config.high_threshold,
    )

    num_stars_low = 0 if sources_low is None else len(sources_low)
    num_stars_high = 0 if sources_high is None else len(sources_high)

    print(
        f"Detected {num_stars_low} stars "
        f"for threshold={config.low_threshold}, "
        f"fwhm={config.fwhm}"
    )

    print(
        f"Detected {num_stars_high} stars "
        f"for threshold={config.high_threshold}, "
        f"fwhm={config.fwhm}"
    )

    if num_stars_high > 0:
        non_zero_stars.append(str(fts_file))

    elif num_stars_low > 0:
        zero_stars_only_th10.append(str(fts_file))

        df = sources_low.to_pandas()
        brightest = df.sort_values("flux", ascending=False)

        print("Top 10 brightest sources:")
        print(brightest.head(10))

    else:
        zero_stars_th5.append(str(fts_file))

    print("####################################")


def main() -> None:
    config = read_config()

    zero_stars_th5 = []
    zero_stars_only_th10 = []
    non_zero_stars = []

    for input_dir in config.fts_input:

        fts_dir = Path(input_dir)

        if not fts_dir.exists():
            print(f"Directory does not exist: {fts_dir}")
            continue

        for fts_file in sorted(fts_dir.glob("*.fts")):
            process_fts_file(
                fts_file=fts_file,
                config=config,
                zero_stars_th5=zero_stars_th5,
                zero_stars_only_th10=zero_stars_only_th10,
                non_zero_stars=non_zero_stars,
            )

    print()
    print("========== SUMMARY ==========")
    print("non zero stars:", non_zero_stars)
    print("zero stars only high threshold:", zero_stars_only_th10)
    print("zero stars low threshold:", zero_stars_th5)


if __name__ == "__main__":
    main()