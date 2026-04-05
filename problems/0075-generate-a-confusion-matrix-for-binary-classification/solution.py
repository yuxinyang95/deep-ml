
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	tp = tn = fp = fn = 0
	for t, p in data:
		if t == p == 1:
			tp += 1
		elif t == p == 0:
			tn += 1
		elif t == 1 and p == 0:
			fn += 1
		else:
			fp += 1
	return [[tp, fn], [fp, tn]]