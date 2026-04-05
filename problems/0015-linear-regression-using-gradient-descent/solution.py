import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros
    # Linear expression
    # y = wx + b
    # L(thetha) = (WX - Y) ** 2
    # Your code here: implement gradient descent
    # Gradiant descnet is using derivatie of L theta to updata
    # 1 / m * XT * (x thest - Y)
    # theta = theta - alpha * grad
    for _ in range(iterations):
        grad = (1 / m) * X.T @ (X @ theta - y)
        theta = theta - grad * alpha
    return theta.flatten()