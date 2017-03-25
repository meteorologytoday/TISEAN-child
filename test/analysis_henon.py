import numpy as np
import DataSeries

X = np.fromfile("output/traj_X.bin", dtype='<f4')[1000:1000+65536]

ds = DataSeries.DataSeries(X, 3, 50)
ds.printDelayMap("printtest.txt")
