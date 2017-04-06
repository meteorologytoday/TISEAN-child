from DataSeries import DataSeries as DS
import matplotlib.pyplot as plt
import numpy as np
import sys

x = np.loadtxt("data/henon.txt", usecols=(1,), unpack=True)

x = x[::20]

ds = DS(x, n=2, delay=1)
dm = ds.getDelayedMap()


pt = [16.4, -1.5]
pt = [-14, 11]
neighbors = ds.getNeighborsRank(pt)[0:10]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(dm[:,0], dm[:,1], color='r', zorder=1)

ax.scatter([pt[0]], [pt[1]], marker='*', color='#00ff00', zorder=95)
ax.text(pt[0], pt[1]*0.95, 'anchor', zorder=95, horizontalalignment='center', verticalalignment='top')

for i, neighbor in enumerate(neighbors):
	pt = dm[neighbor[0]]
	ax.text(pt[0], pt[1], "%d" % (i, ), zorder=99, verticalalignment='center', horizontalalignment='center')


plt.show()


