import numpy as np


# input data

def mutual(timeseries, lag, partitions):
	datum = np.zeros( len(in) ,dtype=int)
	datum = timeseries * partitions

	for i, data in enumerate(datum):
		if data < 0:
			datum[i] = 0
		else if data > partitions - 1:
			datum[i] = partitions - 1

	lag_datum = datum[lag:] #  [ -------------------------   ]
	datum = datum[:-lag]    #  [    -------------------------]

	# pi pj pij
	pi = np.zeros(partitions, dtype=float)
	pj = pi.copy()
	pij = np.zeros((partitions, partitions), dtype=float)

	for data in datum:
		pi[data] += 1

	for lag_data in lag_datum:
		pj[lag_data] += 1

	for data in datum:
		for lag_data in lag_datum:
			if data == lag_data:
				pij[data, lag_datum] += 1

	minfo = 0.0

	for i in range(0, partitions):
		for j in range(0, partitions):
			minfo += pij(i,j) * np.log(pij(i,j) / pi(i) / pj(j))


	return minfo

