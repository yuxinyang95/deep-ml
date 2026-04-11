
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	return round(np.sqrt(np.mean((y_true - y_pred) ** 2)), 3)
