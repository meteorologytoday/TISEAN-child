import numpy as np


def NNM_vec(dataseries, neighbors, start, steps, weight=None):
	""" 
	This function predicts by finding NN and using their velocity vectors average
	to determine next move.

	<dataseries>
		An instance of DataSeries

	<neighbors>
		Number of neighbors.

	<start>
		Starting point of prediction.

	<steps>
		How many steps to predict?

	<weight>
		An 1-dimensional array consisting <neighbors> elements. This array specifies
		the weighting of nearest neighbors. Default weighting is for all neighbors.
		Also, weightings are expected to be positive numbers.
	
	"""

	if weight is None:
		weight = np.zeros(neighbors) + 1.0

	total_weight = sum(weight)
	current_pt = np.array(start, dtype=np.float)
	pred = np.zeros((steps, dataseries.n))
	data = dataseries.dm

	for i in range(steps):
		NNs = dataseries.getNeighborsRank(current_pt)
		vecs = []

		for j, NN in enumerate(NNs):
			if len(vecs) == neighbors:
				break

			# Skip because the first element has no predecessor.
			if NN[0] == 0:
				continue

			vecs.append(np.array(data[NN[0]]) - np.array(data[NN[0]-1]))


		avg_vec = np.zeros(dataseries.n)
		for j in range(len(vecs)):
			avg_vec += vecs[j] * weight[j]

		avg_vec /= total_weight

		pred[i] = current_pt + avg_vec
		current_pt[:] = pred[i]

	return pred
			
			
def NNM_mc(dataseries, neighbors, start, steps, weight=None):
	""" 
	This function predicts by finding NN and using their average position
	to determine next move.

	<dataseries>
		An instance of DataSeries

	<neighbors>
		Number of neighbors.

	<start>
		Starting point of prediction.

	<steps>
		How many steps to predict?

	<weight>
		An 1-dimensional array consisting <neighbors> elements. This array specifies
		the weighting of nearest neighbors. Default weighting is for all neighbors.
		Also, weightings are expected to be positive numbers.
	
	"""

	if weight is None:
		weight = np.zeros(neighbors) + 1.0

	total_weight = sum(weight)
	current_pt = np.array(start, dtype=np.float)
	pred = np.zeros((steps, dataseries.n))
	data = dataseries.dm

	for i in range(steps):
		NNs = dataseries.getNeighborsRank(current_pt)
		vecs = []

		for j, NN in enumerate(NNs):
			if len(vecs) == neighbors:
				break

			# skip because the last point has no future reference
			if NN[0] == dataseries.dm_len-1:
				continue

			vecs.append(np.array(data[NN[0]+1]))


		avg_vec = np.zeros(dataseries.n)
		for j in range(len(vecs)):
			avg_vec += vecs[j] * weight[j]

		avg_vec /= total_weight

		pred[i] = avg_vec
		current_pt = np.array(pred[i])

	return pred
			
			

	
	
	
		
