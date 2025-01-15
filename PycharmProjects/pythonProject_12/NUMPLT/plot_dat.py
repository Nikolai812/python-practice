import numpy as np
import matplotlib.pyplot as plt

input_file1 = "input1.dat"
input_file2 = "input2.dat"
data1 = np.loadtxt(input_file1)
data2 = np.loadtxt(input_file2)

#Splitting input data into arrays

t = data1[:, 0]
v = data1[:, 1]
delta = data1[:, 2]

plt.figure()
plt.subplot(211)
plt.plot(t,v, "bs", markersize=4)
plt.subplot(212)
plt.plot(data2[:, 0], data2[:, 1], "r", data2[:, 0], data2[:, 2], "g", data2[:, 0], data2[:, 3], "b")
plt.show()

#output_file =  np.savetxt("output.txt", np.column_stack((t,v,delta)), "%2f %3f %3f")

#print(f"Data has been read from '{input_file_name}' and written to '{output_file}'.")


