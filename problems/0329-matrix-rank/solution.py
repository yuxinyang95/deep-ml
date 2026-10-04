import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    A = A.astype(float).copy()
    m, n = A.shape

    rank = 0
    row = 0

    for col in range(n):
        pivot = row + np.argmax(np.abs(A[row:, col]))

        if abs(A[pivot, col]) <= tol:
            continue

        A[[row, pivot]] = A[[pivot, row]]

        for r in range(row + 1, m):
            factor = A[r, col] / A[row, col]
            A[r] -= factor * A[row]

        rank += 1
        row += 1

        if row == m:
            break

    return rank