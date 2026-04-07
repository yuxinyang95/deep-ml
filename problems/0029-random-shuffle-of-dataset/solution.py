import numpy as np

def shuffle_data(X, y, seed=None):
    if len(X) != len(y):
        raise ValueError("X and y must have the same number of samples.")

    if seed is not None:
        np.random.seed(seed)

    indices = np.random.permutation(len(X))
    return X[indices], y[indices]