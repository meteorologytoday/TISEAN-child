from DataSeries import DataSeries as DS
from Entropy import calEntropySeries
import matplotlib.pyplot as plt
import numpy as np
import sys

print("Processing...")

year, mon, x = np.loadtxt("data/mei.txt", usecols=(0, 1, 2), dtype=float, unpack=True)
t = year + mon/12.0

#t, x = np.loadtxt("data/MackeyGlass.txt", usecols=(0, 1), dtype=float, unpack=True)
#t = t[::10]
#x = x[::10]

print("Generating graph...")
fig, (ax1, ax2) = plt.subplots(2)

# top panel
ax1.plot(t, x, color='r', zorder=1)

# bottom panel
window_size = 24
ent = calEntropySeries(x, window_size, intervals=10)
ax2.plot(t[window_size-1:], ent, color='k')
plt.show()


