import numpy as np


# input data

def mutual(timeseries, span, lag, partitions):
	datum = np.zeros( len(timeseries), dtype=int )
	datum = timeseries * partitions

	for i, data in enumerate(datum):
		if data < 0:
			datum[i] = 0
		elif data > partitions - 1:
			datum[i] = partitions - 1
		else:
			datum[i] = int(datum[i])

	lag_datum = datum[lag:]            #  [ -------------------------   ]
	datum = datum[0:len(datum)-lag]    #  [    -------------------------]
	N = len(datum)

	# pi pj pij
	pi = np.zeros(partitions, dtype=float)
	pj = pi.copy()
	pij = np.zeros((partitions, partitions), dtype=float)

	for data in datum:
		pi[int(data)] += 1

	for lag_data in lag_datum:
		pj[int(lag_data)] += 1

	for i in range(0, N):
		a = int(datum[i])
		b = int(lag_datum[i])

		pij[a, b] += 1
		#pij[b, a] = pij[a, b]

	pi /= N
	pj /= N
	pij /= N

	minfo = 0.0

	for i in range(0, partitions):
		for j in range(0, partitions):
			if pij[i,j] != 0 and pi[i] != 0 and pj[j] != 0:
				minfo += pij[i,j] * np.log2(pij[i,j] / pi[i] / pj[j])

	#minfo *= span ** 2.0 # dpi dpj

	return minfo

