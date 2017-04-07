import numpy as np

steps = 10000
init = np.array([0.0, 1.0, 0.0])
dt = 0.01

shifts = np.arange(0, 220, 20)

def rk4(x, dxfunc, dt):
	dx1 = dt * dxfunc(x)
	dx2 = dt * dxfunc(x + dx1 / 2.0)
	dx3 = dt * dxfunc(x + dx2 / 2.0)
	dx4 = dt * dxfunc(x + dx3)
	return x + (dx1 + 2.0 * dx2 + 2.0 * dx3 + dx4) / 6.0


sigma, gamma, beta = 10.0, 28.0, 8.0/3.0
def DynamicalSystem(x):
	global sigma, gamma, beta
	X, Y, Z = x
	return np.array([sigma * (Y - X), X * (gamma - Z) - Y, X * Y - beta * Z])


x = init.copy()

record = np.zeros((3, steps), dtype='<f4')
for i in range(0, steps):
	x = rk4(x, DynamicalSystem, dt)
	record[0, i], record[1, i], record[2, i] = x[0], x[1], x[2]

with open("Lorenz.txt", 'w') as f:
	f.write("#time x y z\n")
	for i in range(0, steps):
		f.write("%.5e %.5e %.5e %.5e\n" % (dt * i, record[0,i], record[1,i], record[2,i]))
