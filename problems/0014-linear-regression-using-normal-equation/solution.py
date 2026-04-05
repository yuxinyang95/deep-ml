import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	# θ=(XTX)−1XTy
	y = np.array(y).reshape(-1, 1)
	X = np.array(X)
	theta = np.linalg.pinv(X.T @ X) @ X.T @ y
	return np.round(theta.flatten(), 4)