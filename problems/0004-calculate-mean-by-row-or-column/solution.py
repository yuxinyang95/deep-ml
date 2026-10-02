def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	rows = len(matrix)
	columns = len(matrix[0])
	if mode == "row":
		return [sum(x) / columns for x in matrix ]
	else:
		return [sum(x) / rows for x in zip(*matrix)]