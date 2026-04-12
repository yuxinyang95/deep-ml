def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	count = {}
	for color in apples:
		count[color] = count.get(color, 0) + 1
	result = 0
	n = len(apples)
	for val in count.values():
		result += (val / n) ** 2
	return 1 - result