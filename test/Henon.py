import numpy as np

steps = 1048576 + 1000
#steps = 1000
init = np.array([10.0, 0.0, 0.0])
dt = np.pi / 100.0

shifts = np.arange(0, 220, 20)

def rk4(x, dxfunc, dt):
	dx1 = dt * dxfunc(x)
	dx2 = dt * dxfunc(x + dx1 / 2.0)
	dx3 = dt * dxfunc(x + dx2 / 2.0)
	dx4 = dt * dxfunc(x + dx3)
	return x + (dx1 + 2.0 * dx2 + 2.0 * dx3 + dx4) / 6.0


a, b, c = 0.15, 0.20, 10.0
def henon(x):
	X, Y, Z = x
	return np.array([- Z - Y, X + a * Y, b + Z * (X - c)])


x = init.copy()

record = np.zeros((3, steps), dtype='<f4')
for i in range(0, steps):
	x = rk4(x, henon, dt)
	record[0, i], record[1, i], record[2, i] = x[0], x[1], x[2]


record[0,:].tofile("output/traj_X.bin")
record[1,:].tofile("output/traj_Y.bin")
record[2,:].tofile("output/traj_Z.bin")

record.transpose().tofile("output/traj_XYZ.bin")


for shift in shifts:
	n = steps - 2 * shift
	xx = np.zeros((3, n), dtype='<f4')
	for i, var in enumerate(['X', 'Y', 'Z']):
		xx[0, :] = record[i,         0 : n            ]
		xx[1, :] = record[i,     shift : n +     shift]
		xx[2, :] = record[i, 2 * shift : n + 2 * shift]

		xx.transpose().tofile("output/traj_%s_shift_%d.bin" % (var, shift,))
