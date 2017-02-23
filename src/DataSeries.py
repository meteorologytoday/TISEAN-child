import numpy as np



class DataSeries:
	def __init__(self, data, n, delay):
		"""
		# PARAMETERS
		<data>
			A 1-dimensional array of float which will be copied.

		<n>
			Dimension of embedding.

		<delay>
			An integer representing time delay. For example, if 
            n = 3 and delay = 5, and len(data) = 100, then this
			means there are 3 series, each with length 90, i.e.

			X1 = [ data[ 0], data[ 1], ..., data[89] ]
			X2 = [ data[ 5], data[ 6], ..., data[94] ]
			X3 = [ data[10], data[11], ..., data[99] ]

		"""
		self.data = np.array(data)
		self.n = n
		self.delay = delay

	def lazyBuild(self):
		l = len(self.data)
		new_data = np.zeros((self.n, l - self.delay * (self.n - 1)), dtype=np.float32)
		for i in range(0, self.n):
			new_data[i, :] = self.data[ i*self.delay : l - (self.n - 1 + i) * self.delay ]

		return new_data

	def build(self):
		self.dm = self.lazyBuild()
		self.dm_len = self.dm.shape[1]

	def findNearestNeighbors(self, order, point):
		"""
		# PARAMETERS
		<order>
			How many neighbors.

		<point>
			A tuple/list of numbers representing target point in
			<self.n>-dimensional embedding space.

		# RETURN VALUE
			A list of integers which are indices of neighbors
			found in original data series.
		"""
		neighbors = np.array([])
		if self.dm is None:
			self.build()
		
		dist = np.zeros(self.dm_len)
		for i in range(0, self.dm_len):
			dist[i] = (((self.dm[i, :] - point) ** 2.0).sum()) ** 0.5

		

		return 
