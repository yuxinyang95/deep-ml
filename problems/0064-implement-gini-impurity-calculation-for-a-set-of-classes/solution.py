
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	count = {}
	for val in y:
		count[val] = count.get(val, 0) + 1
	result = 0
	total = len(y)
	for val in count.values():
		result += (val / total) ** 2	
	return round(1 - result,3)