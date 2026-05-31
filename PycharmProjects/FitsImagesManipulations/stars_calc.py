from astropy.io import fits
from photutils.detection import DAOStarFinder
from astropy.stats import sigma_clipped_stats

data = fits.getdata("image.fts")

mean, median, std = sigma_clipped_stats(data)

finder = DAOStarFinder(
    threshold=5*std,
    fwhm=3.0
)

sources = finder(data - median)

print(len(sources))