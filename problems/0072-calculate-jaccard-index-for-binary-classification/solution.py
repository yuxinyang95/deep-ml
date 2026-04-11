
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code her
	total = np.sum(y_true) + np.sum(y_pred)
	common = np.sum((y_true == 1) & (y_pred == 1))
	result = common / (total - common)
	return round(result, 3)
