import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if x.ndim != 1:
		return
	if n_col is None:
		n_col = np.max(x) + 1
	
	result = np.zeros((len(x), n_col), dtype = int)
	result[np.arange(len(x)), x] = 1
	return result