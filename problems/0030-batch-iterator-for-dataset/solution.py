import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
    if y is not None and len(X) != len(y):
        raise ValueError("X and y must have the same number of samples.")

    result = []
    for i in range(0, len(X), batch_size):
        if y is not None:
            result.append((X[i:i + batch_size], y[i:i + batch_size]))
        else:
            result.append(X[i:i + batch_size])
    return result