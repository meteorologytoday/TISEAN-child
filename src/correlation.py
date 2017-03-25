import numpy as np

def euclidean_dist_square(x, y):
	"""
		Notice that x and y are assumed to be numpy 1D array.
	"""
	return np.sum((x - y) ** 2.0)

def calCorrelation(ds, l, d = euclidean_dist_square):
	"""
		This function calculate the correlation function
		
		C(l) = (1 / N^2) * {number of pairs (i,j) whose 
               distance d(X_i, X_j) is less than l }

		where N is the length of data series {X_1, X_2, ..., X_N}.

		The shape of data series is assumed to be (D, N) where D
		is the dimension of sample space and N is defined as above.

	"""

	cnt = 0
	(D, N) = ds.shape
		
	for i in range(0, N-1):
		for j in range(i+1, N):
			if d(ds[:, i], ds[:, j]) < l:
				cnt += 1

	return float(cnt) / float(N) ** 2.0
