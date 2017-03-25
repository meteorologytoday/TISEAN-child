from DataSeries import DataSeries as DS
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#x,y,z = np.loadtxt("data/henon.txt", usecols=(1,2,3), unpack=True)
x = np.loadtxt("data/pdo.txt", usecols=(2,), unpack=True)

x = x[-100:]

ds = DS(x, 3, 1)

dm = ds.getDelayedMap()

fig = plt.figure()
ax = fig.add_subplot(111)
ax = fig.add_subplot(111, projection='3d')

#ax.scatter(dm[0,:], dm[1,:])
#ax.scatter(dm[0,:], dm[1,:], dm[2,:])
ax.plot(dm[0,:], dm[1,:], dm[2,:])

plt.show()


