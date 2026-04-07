import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = np.sum((y_true == 1) & (y_pred == 1))

	return tp / np.sum(y_pred == 1)
