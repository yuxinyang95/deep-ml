import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	y_pred = X @ w
	loss = np.mean((y_pred - y_true) ** 2)
	return loss + alpha * np.sum(w ** 2)