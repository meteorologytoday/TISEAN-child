import numpy as np


dt = 0.01

beta = 2
gamma = 1
n = 9.65
tau = 2

dn = int(tau / dt)
steps = int(10000 + dn)

pseudo = np.zeros(dn, dtype=float) + 0.8

def rk4(x, dxfunc, dt):
	dx1 = dt * dxfunc(x)
	dx2 = dt * dxfunc(x + dx1 / 2.0)
	dx3 = dt * dxfunc(x + dx2 / 2.0)
	dx4 = dt * dxfunc(x + dx3)
	return x + (dx1 + 2.0 * dx2 + 2.0 * dx3 + dx4) / 6.0


def DynamicalSystem(x):
	global beta, gamma, n
	X, Y = x
	return np.array([beta * Y / (1.0 + Y ** n) - gamma * X, 0.0])


record = np.zeros(steps, dtype=float)
x = np.array([1.0, 0.0], dtype=float) # Notice the continuity of pseudo and x
for i in range(0, steps):
	x[1] = pseudo[i] if i < dn else record[i - dn]
	#print("Step %d: x = (%.2e, %.2e)" % (i, x[0], x[1]))
	x = rk4(x,  DynamicalSystem, dt)
	record[i] = x[0]

with open("MackeyGlass.txt", 'w') as f:
	f.write("#beta = %.3e, gamma = %.3e, n = %.3e, tau = %.e\n" % (beta, gamma, n, tau))
	f.write("#time x\n")
	for i in range(dn, steps):
		f.write("%.5e %.5e\n" % (dt * (i - dn), record[i]))


