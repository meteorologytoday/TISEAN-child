import numpy as np
from mutual import mutual

year, mon, X  = np.loadtxt("mei.txt", dtype={'names': ('year', 'mon', 'mei'), 'formats': ('f4', 'f4', 'f4')}, unpack=True)

data_dir = 'output'

# normalize into [0, 1]
span = [np.amin(X), np.amax(X)]

X -= span[0]
tot_span = span[1] - span[0]
X /= tot_span

print("Span: %.2f" % (tot_span,))

partitions = 32
shifts = np.arange(0, 120)
minfo = np.zeros(len(shifts))
for i in range(0, len(shifts)):
	minfo[i] = mutual(X, tot_span, shifts[i], partitions)
	print("shift: %.2f, \tminfo: %.2e" % (shifts[i], minfo[i]))


with open("minfo_mei.txt", "w") as f:
	for i in range(0, len(minfo)):
		f.write("%.3e %.3e\n" % (shifts[i], minfo[i]))
