import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# Your code here
	# P(y = 1 | x) = sigmod(Wtx + b)
	# simogd = 1 / (1 + e ** (-z)
	if X.shape[1] != weights.shape[0]:
		raise ValueError("dimension not the same")
	logits = X @ weights + bias
	prob = 1 / (1 + np.exp(-logits))
	return (prob >= 0.5).astype(int)
