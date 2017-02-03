import numpy as np
from mutual import mutual

part = 20
data_dir = 'output'
X = np.fromfile("%s/traj_X.bin" % (data_dir,), dtype='<f4')[1000:1000+65536]
# normalize into [0, 1]
span = [np.amin(X), np.amax(X)]

X -= span[0]
tot_span = span[1] - span[0]
X /= tot_span

print("Span: %.2f" % (tot_span,))

orbit = 193.3
partitions = 32
shifts = np.linspace(0, 5, num=301)
minfo = np.zeros(len(shifts))
for i in range(0, len(shifts)):
	shift = int(shifts[i] * orbit)
	minfo[i] = mutual(X, tot_span, shift, partitions)
	print("shift: %.2f (%.2f), \tminfo: %.2e" % (shift, shifts[i], minfo[i]))


with open("minfo.txt", "w") as f:
	for i in range(0, len(minfo)):
		f.write("%.3e %.3e\n" % (shifts[i], minfo[i]))
