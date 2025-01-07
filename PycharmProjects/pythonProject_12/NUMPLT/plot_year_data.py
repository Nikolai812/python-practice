import numpy as np
import matplotlib.pyplot as plt




def f(t):
    return np.exp(-t*t /10) * np.cos(0.5 * np.pi * t)


first_list = [1, 2, 3]
first_array = np.array([1, 2, 3])

range_list = [r for r in range(2, 20, 3)]

comp_list = [x * x for x in range(5)]

t1 = np.arange(0,365, 0.2)
t2 = np.arange(0, 365, 0.2)


plt.figure()
plt.plot(t1, f(t1 - 150), 'rs',markersize=1)
plt.plot(t2, 0.5 * f(t2 - 200), 'g^', markersize=0.5)
plt.xlim(120, 220)
plt.xlabel("Days")
plt.ylabel("Y-axis")
plt.show()


