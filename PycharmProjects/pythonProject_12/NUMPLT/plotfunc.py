import numpy as np
import matplotlib.pyplot as plt


def xarray(n, a=0.0, b=1.0):
    d = (b - a) / n
    i_list = [i for i in range(n)]
    x = [(a + d * (i + 0.5)) for i in i_list]
    return x


def y_lin(x_data, a=1.0, b=0.0):
    return [a * xi + b for xi in x_data]


def f(t):
    return np.exp(-t*t) * np.cos(2 * np.pi * t)


first_list = [1, 2, 3]
first_array = np.array([1, 2, 3])

range_list = [r for r in range(2, 20, 3)]

comp_list = [x * x for x in range(5)]

xdata = xarray(10, 2.0, 3.0)
y_data = y_lin(xdata, 2.0, 3.0)

#plt.plot(xdata, y_data)
#plt.show()
t1 = np.arange(-3.0, 3.0, 0.1)
t2 = np.arange(-2.0, 4.0, 0.05)


plt.figure()
#plt.subplot(211)
plt.plot(t1, f(t1), 'rs', t2, 0.5 * f(t2 - 1), 'g^')
plt.show()

print(xdata)
print (y_data)
print(range_list)
print(comp_list)

