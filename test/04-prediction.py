from DataSeries import DataSeries as DS
import Prediction
import matplotlib.pyplot as plt
import numpy as np
import sys

print("Processing...")

#year, mon, x = np.loadtxt("data/mei.txt", usecols=(0, 1, 2), dtype=float, unpack=True)

t, x = np.loadtxt("data/Lorenz.txt", usecols=(0, 1), dtype=float, unpack=True)

#t = t[-240:]
#x = x[-240:]

resolution = 10
predict_range = 50
delay = 2
n = 3
ref_neighbors=6
weight = [ref_neighbors - i for i in range(ref_neighbors)]
weight = np.zeros(ref_neighbors) + 1
weight = [ i for i in range(ref_neighbors)]
weight = None
pred_span = predict_range + (n-1) * delay

x = x[::resolution] # should be 499 data
t = t[::resolution] # should be 499 data



x_data = x[:-predict_range]
t_data = t[:-predict_range]

x_true = x[-predict_range:]
t_true = t[-predict_range:]

t_pred = t[-pred_span:]
ds = DS(x_data, n=n, delay=delay)
dm = ds.getDelayedMap()

pt = dm[-1]
future = Prediction.NNM_mc(ds, ref_neighbors, pt, pred_span, weight=weight)

print("Generating graph...")
fig, (ax1, ax2) = plt.subplots(2)

# top panel
ax1.plot(dm[:,0], dm[:,1], color='r', zorder=1)
ax1.scatter([pt[0]], [pt[1]], marker='*', color='#00ff00', zorder=95)

for i in range(future.shape[0]):
	prev = ( np.array(pt) if i==0 else future[i-1] )
	delta = future[i] - prev
	delta_length = (delta**2.0).sum()**0.5
	delta *= 1.0 - 1.0 / delta_length
	ax1.arrow(prev[0], prev[1], delta[0], delta[1], head_width=0.5, head_length=1.0, zorder=94, fc='#888888', ec='#888888')
	ax1.scatter([future[i,0]], [future[i,1]], marker='^', color='#0000aa', zorder=95)

# bottom panel
t_span = t_pred[-1] - t_pred[0]
data_range = np.array([np.amin(x_data), np.amax(x_data)])
data_span = data_range[1] - data_range[0]
ax2.set_xlim([t_pred[0] - 0.1 * t_span, t_pred[-1] + 0.1 * t_span])
ax2.set_ylim([data_range[0] - 0.1 * data_span, data_range[1] + 0.1 * data_span])
ax2.scatter(t_data, x_data, color='#ff0000', marker='^')
ax2.scatter(t_true, x_true, color='#ff0000', marker='o')
ax2.scatter(t_pred, future[:, 0], marker='s', color='#0000aa')
ax2.plot([t_pred[0]]*2, data_range, color='#888888', dashes=(10,5))
ax2.plot([t_true[0]]*2, data_range, color='#888888', dashes=(10,5))
plt.show()


