import numpy as np

def calEntropy(data, lower=0.0, upper=1.0, intervals=10, normalize=True):
	if normalize:
		upper = np.amax(data)
		lower = np.amin(data)

	if upper - lower == 0.0:
		return 0.0

	data = ((data - lower) / (upper - lower) * intervals).astype(int)
	cnt = np.zeros((intervals,), dtype=float)
	for _, val in enumerate(data):
		if val >= intervals:
			val = intervals - 1
		cnt[val] += 1

	cnt /= len(data)

	entropy = 0.0
	for i, val in enumerate(cnt):
		entropy += 0 if val <= 0.0 else val * np.log(val)


	return - entropy

def calEntropySeries(data, window_size, lower=0.0, upper=1.0, intervals=10, normalize=True):
	if normalize:
		upper = np.amax(data)
		lower = np.amin(data)

	if upper - lower == 0.0:
		return 0.0
	
	data = (data - lower) / (upper - lower)
	e = np.zeros((len(data)-window_size+1,), dtype=float)

	for i, _ in enumerate(e):
		e[i] = calEntropy(data[i:i+window_size], lower=0.0, upper=1.0, intervals=intervals, normalize=False)

	return e 
	
