def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    rows, columns = len(a), len(a[0])
    result = [[0] * rows for _ in range(columns)]
    for row in range(rows):
        for col in range(columns):
            result[col][row] = a[row][col]
    return result