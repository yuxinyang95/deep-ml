
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	common = np.sum((y_true == 1) & (y_pred == 1))
	total = np.sum(y_true) + np.sum(y_pred)
	if total == 0:
		return 0
	res = 2 * common / total
	return round(res, 3)
