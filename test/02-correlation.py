from DataSeries import DataSeries as DS
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from correlation import calCorrelation

X = np.loadtxt("data/henon.txt", usecols=(1,2,3), unpack=True)
#x = np.loadtxt("data/pdo.txt", usecols=(2,), unpack=True)

#x = x[-500:]
#sup = np.max(x)
#inf = np.min(x)

#x = x / (sup - inf)


#ds = DS(x, 3, 50)
#dm = ds.getDelayedMap()

dm = X[:, -500:] / (np.amax(X) - np.amin(X))



boxes = np.array([0.01 * (i+1) for i in range(0, 20)])
cor = boxes.copy()

for i, box in enumerate(boxes):
	print("Calculate for box = %.2f" % (box,))
	cor[i] = calCorrelation(dm, box)

cor = np.log(cor)
boxes = np.log(boxes)
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(boxes, cor, marker='o')

plt.show()


