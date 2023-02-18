# post-processing routine using matplotlib

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, signal

# name of the file with scalar data
postfile = 'results/transient_results.csv'

t, M, iu, iv, iw, uu, uv, uw = np.loadtxt(postfile, unpack=True,
usecols=(5,2,6,13,20,8,15,22))

i1,i2,i3,i4,i5,i6,i7,i8,i9,i10 = np.loadtxt(postfile, unpack=True,
usecols=(27,43,49,55,61,67,73,79,85,91))

plt.figure()
plt.plot(t, iu)
plt.grid(True)
plt.hold(True)
plt.plot(t, iv)
plt.plot(t, iw)
plt.ylabel("Current")

plt.figure()
plt.plot(t, M*4*0.160)
plt.grid(True)
plt.ylabel("Torque")

plt.figure()
plt.plot(t, uu, label="U_u")
plt.grid(True)
plt.hold(True)
plt.plot(t, uv, label="U_v")
plt.plot(t, uw, label="U_w")
plt.ylabel("Voltage")
plt.legend(loc='best')

plt.figure()
plt.plot(t, i4, label="i4")
plt.grid(True)
plt.hold(True)
plt.plot(t, i5, label="i5")
plt.plot(t, i6, label="i6")
plt.plot(t, i7, label="i7")
plt.plot(t, i3, label="i3")
plt.plot(t, i8, label="i8")
plt.plot(t, i1, label="i1")
plt.plot(t, i2, label="i2")
plt.plot(t, i9, label="i9")
plt.plot(t, i10, label="i10")
plt.plot(t, i1+i2+i3+i4+i5+i6+i7+i8+i9+i10, label="sum of pole currents")
plt.ylabel("Rotor Current")
plt.legend(loc='best')
plt.xlabel("Time, $t$ [s]")

plt.show()
