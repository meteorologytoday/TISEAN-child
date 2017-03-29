from DataSeries import DataSeries as DS
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from correlation import calCorrelation
from scipy import stats
import sys

#X = np.loadtxt("data/henon.txt", usecols=(1,2,3), unpack=True)
#x = np.loadtxt("data/pdo.txt", usecols=(2,), unpack=True)
#x = np.loadtxt("data/mei.txt", usecols=(2,), unpack=True)

x = np.random.rand(2000)

sup = np.max(x)
inf = np.min(x)

x = x / (sup - inf)

print(x)

ds = DS(x, n=int(sys.argv[1]), delay=12)
dm = ds.getDelayedMap()

#dm = X[:, -500:] / (np.amax(X) - np.amin(X))



#boxes = np.exp(linspace(0, 1, num=21)[1:]) # ln(0) is undefined so must be avoided

boxes = np.array([0.1 * (i+1) for i in range(0, 10)])
cor = boxes.copy()

for i, box in enumerate(boxes):
	print("Calculate for box = %.2f" % (box,))
	cor[i] = calCorrelation(dm, box)

print(cor)

cor = np.log(cor)
boxes = np.log(boxes)

slope, intercept, r_value, p_value, std_err = stats.linregress(boxes, cor)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(boxes, cor, marker='o', color='b')
ax.plot(boxes, slope * boxes + intercept, color='r')
ax.text(0.5, 0.5, r'$y = %.2f x + %.2f, r = %.2f $' % (slope, intercept, r_value),transform=ax.transAxes)

plt.show()


