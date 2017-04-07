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

			The data is arranged in [time, dimension] format.

		"""
		self.data = np.array(data)
		self.n = n
		self.delay = delay
		self.build_flag = False

	def updateDim(n):
		if self.n != n:
			self.n = n
			self.build_flag = False

	def updateDelay(delay):
		if self.delay != delay:
			self.delay = delay
			self.build_flag = False

	def build(self):
		if self.build_flag == True:
			return

		l = len(self.data)
		self.dm_len = l - self.delay * (self.n - 1)
		self.dm = np.zeros((self.dm_len, self.n), dtype=np.float32)
		for i in range(0, self.n):
			self.dm[:, i] = self.data[ i*self.delay : l - (self.n - 1 - i) * self.delay ]


		self.dm_len = self.dm.shape[0]
		self.build_flag = True


	def getDelayedMap(self):
		self.build()
		return np.array(self.dm)


	def getDistMap(self):
		"""
			Building a distance map which is a matrix representing the dist between
			the i-th and j-th point based on euclidean metric.
		"""

		self.build()

		distmap = np.zeros((self.dm_len, self.dm_len))
		for i in range(0, self.dm_len):
			for j in range(i, self.dm_len):
				distmap[i,j] = (((self.dm[i,:] - self.dm[j,:]) ** 2.0).sum()) ** 0.5
				
				 # for i=j just do it again since speed is almost the same
				distmap[j,i] = distmap[i,j]

		return distmap

	def getNeighborsRank(self, point):
		"""

		    This function returns the nearest neighbors based on
	    Euclidean distance function.

		# PARAMETERS
		<point>
			A tuple/list of numbers representing target point in
			<self.n>-dimensional embedding space.

		# RETURN VALUE
			A list of (i, point) pairs in which the first elements are indices
			of neighbors and second elements are distance.
		"""

		self.build()
		neighbors = np.array([])
			
		rank = [None for _ in range(0, self.dm_len)]
		point = np.array(point)
		for i in range(0, self.dm_len):
			rank[i] = [i, (((self.dm[i,:] - point)**2.0).sum())**0.5]
			

		rank.sort(key=lambda x: x[1])

		return rank

	def printDelayMap(self, filename):
		self.build()
		with open(filename, "w") as fh:
			for i in range(0, self.dm_len):
				for j in range(0, self.n):
					fh.write("%.3e " % (self.dm[i, j],))
				
				fh.write("\n")




