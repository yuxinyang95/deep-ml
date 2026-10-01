import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    # g'(x) * f(x) - g(x)h'(x)
    # h(x) ** 2
    g_x = 0
    h_x = 0
    g_x_d = 0
    h_x_d = 0

    for i in range(len(g_coeffs)):
        power = len(g_coeffs) - i - 1

        g_x += g_coeffs[i] * (x ** power)

        if power != 0:
            g_x_d += g_coeffs[i] * power * (x ** (power - 1))

    for i in range(len(h_coeffs)):
        power = len(h_coeffs) - i - 1

        h_x += h_coeffs[i] * (x ** power)

        if power != 0:
            h_x_d += h_coeffs[i] * power * (x ** (power - 1))

    return (g_x_d * h_x - g_x * h_x_d) / (h_x ** 2)

