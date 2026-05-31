from astropy.io import fits
import numpy as np
from astropy.stats import sigma_clipped_stats


def measure_background_brightness(fts_file_path):
    """
    Measure the raw mean and median pixel brightness of a FITS image.

    Args:
        fts_file_path (str): Path to the .fts (FITS) file.

    Returns:
        dict: Dictionary containing mean, median, and std of all pixel values.
    """
    with fits.open(fts_file_path) as hdul:
        data = hdul[0].data  # Assuming the image data is in the primary HDU

    flat_data = data.flatten()

    return {
        "mean_background": np.mean(flat_data),
        "median_background": np.median(flat_data),
        "std_background": np.std(flat_data),
    }


def measure_background_brightness_with_sigma_clipping(fts_file_path, sigma=3.0, clip_iterations=5):
    """
    Measure the average background brightness of a FITS image.

    Args:
        fts_file_path (str): Path to the .fts (FITS) file.
        sigma (float): Sigma value for sigma clipping (default: 3.0).
        clip_iterations (int): Number of iterations for sigma clipping (default: 5).

    Returns:
        dict: Dictionary containing mean, median, and std of the background.
    """
    # Open the FITS file
    with fits.open(fts_file_path) as hdul:
        data = hdul[0].data  # Assuming the image data is in the primary HDU

    # Flatten the data for analysis
    flat_data = data.flatten()

    # Calculate sigma-clipped statistics to estimate background
    mean, median, std = sigma_clipped_stats(flat_data, sigma=sigma, maxiters=clip_iterations)

    return {
        "mean_background": mean,
        "median_background": median,
        "std_background": std,
    }

# Example usage
if __name__ == "__main__":
    import os

    fts_dir = "FTS"  # Directory containing .fts files
    for filename in os.listdir(fts_dir):
        if filename.endswith(".fts"):
            fts_file = os.path.join(fts_dir, filename)
            background_stats = measure_background_brightness(fts_file)
            #measure_background_brightness_with_sigma_clipping(fts_file)
            print(f"File: {filename}")
            print(f"Mean Background Brightness: {background_stats['mean_background']}")
            print(f"Median Background Brightness: {background_stats['median_background']}")
            print(f"Standard Deviation: {background_stats['std_background']}")
            print("---")  # Separator for clarity