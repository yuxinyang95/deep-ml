def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	# [1, 2] 2 * 2 2 * 1
	# [2, 4] * [1, 2]
	row_a, col_a = len(a), len(a[0])
	if col_a != len(b):
		return -1
	result = [0] * row_a
	for idx, ls in enumerate(a):
		temp = 0
		for i in range(col_a):
			temp += ls[i] * b[i]
		result[idx] = temp
	return result