import numpy as np
from math import factorial
import math
def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    """
    Compute Taylor series approximation for common functions.
    
    Args:
        func_name: Name of function ('exp', 'sin', 'cos')
        x: Point at which to evaluate
        n_terms: Number of terms in the series
    
    Returns:
        Taylor series approximation rounded to 6 decimal places
    """
    result = 0.0
    
    if func_name == "exp":
        for n in range(n_terms):
            result += (x ** n) / math.factorial(n)
    
    elif func_name == "sin":
        for n in range(n_terms):
            result += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    
    elif func_name == "cos":
        for n in range(n_terms):
            result += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    
    else:
        raise ValueError("func_name must be 'exp', 'sin', or 'cos'")
    
    return round(result, 6)