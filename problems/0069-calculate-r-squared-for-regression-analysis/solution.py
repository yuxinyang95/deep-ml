
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    return round(1 - ss_res / ss_total, 3)