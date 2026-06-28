from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder

from dataclasses import dataclass
from configparser import ConfigParser
from pathlib import Path
import shutil


@dataclass
class FTSConfig:
    fts_input: str
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
        fts_input=cfg.get("fts_input", "FTS").strip(),
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


def get_input_directories(root_dir: str) -> list[Path]:
    """
    Return all first-level subdirectories of the configured FTS root.
    """
    root = Path(root_dir)

    if not root.exists():
        raise FileNotFoundError(root)

    return sorted(
        directory
        for directory in root.iterdir()
        if directory.is_dir()
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

def copy_classified_files(config: FTSConfig,
                          non_zero_stars: list[str],
                          zero_stars_only_th10: list[str],
                          zero_stars_th5: list[str]) -> None:
    """
    Copy classified FITS files into the configured output directories.
    """

    if len(config.fts_classified) < 3:
        raise ValueError(
            "fts_classified must contain exactly three directories."
        )

    destinations = [
        Path(config.fts_classified[0]),
        Path(config.fts_classified[1]),
        Path(config.fts_classified[2]),
    ]

    #
    # Create destination directories if they do not exist.
    #
    for dst in destinations:
        dst.mkdir(parents=True, exist_ok=True)

    classifications = [
        (non_zero_stars, destinations[0], "BRIGHT_STARS"),
        (zero_stars_only_th10, destinations[1], "DIM_STARS"),
        (zero_stars_th5, destinations[2], "NO_STARS"),
    ]

    for files, destination, label in classifications:
        for filename in files:
            src = Path(filename)
            dst = destination / src.name

            shutil.copy2(src, dst)

            print(
                f"[COPY] {label:<12} : "
                f"{src} -> {dst}"
            )


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

    for fts_dir in get_input_directories(config.fts_input):
        print(f"\nProcessing {fts_dir}")

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

    if config.dry_run:
        print("\nDry run enabled: no files copied.")
    else:
        print("\nCopying classified FITS files...")
        copy_classified_files(
            config,
            non_zero_stars,
            zero_stars_only_th10,
            zero_stars_th5,
        )


if __name__ == "__main__":
    main()