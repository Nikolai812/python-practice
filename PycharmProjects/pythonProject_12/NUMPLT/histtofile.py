import sys
import matplotlib
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 10000)
plt.hist(x)

# Save the plot to a file
plt.savefig("histogram.png")
print("Histogram saved as 'histogram.png'")