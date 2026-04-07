import numpy as np

def kernel_function(x1, x2):
	# Your code here
    x1 = np.array(x1)
    x2 = np.array(x2)

    if x1.shape != x2.shape:
        raise ValueError("x1 and x2 must have the same shape")

    return np.dot(x1, x2)