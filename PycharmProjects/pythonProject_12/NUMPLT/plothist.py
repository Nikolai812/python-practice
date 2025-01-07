import sys
import matplotlib
matplotlib.use("TkAgg")

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(0.0, 50.0, 250000)

# Specify bin width
bin_width = 50

# Calculate bin edges
#bin_edges = numpy.arange(start=min(x), stop=max(x) + bin_width, step=bin_width)
bin_edges = numpy.arange(-600, 600, step=10)

plt.hist(x,  bins=bin_edges, edgecolor='black') # bins = 50
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with 50 Bins')
plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()