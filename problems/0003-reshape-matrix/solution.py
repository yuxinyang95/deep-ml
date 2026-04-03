import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    rows, cols = new_shape

    flat = [x for row in a for x in row]

    if len(flat) != rows * cols:
        return []

    result = [[0] * cols for _ in range(rows)]

    for i in range(len(flat)):
        r, c = divmod(i, cols)
        result[r][c] = flat[i]

    return result