def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	expected = (1 + n) / 2
	expected_square = (n + 1) * (2 * n + 1) / 6
	return [expected, expected_square - expected ** 2]