import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	result = 0
	for i in range(len(y_true)):
		if y_true[i] == y_pred[i]:
			result += 1
	return result / len(y_true)