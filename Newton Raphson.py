def newtonRaphson(g, x0, eps=1e-8, delta=1e-12, itermax=100):
    """
    Newton-Raphson method for finding the root of a function.

    Parameters:
        g (callable): The function to find the root of. Should return the function value and its derivative.
        x0 (float): The initial guess for the root.
        eps (float): Tolerance for the function value (default: 1e-8).
        delta (float): Tolerance for the change between two consecutive iterates (default: 1e-12).
        itermax (int): Maximum number of iterations (default: 100).

    Returns:
        float: Approximation of the root.

    Raises:
        ValueError: If the maximum number of iterations is reached or if the derivative is too small.
    """
    for _ in range(itermax):
        f, fx = g(x0)
        if abs(fx) < 1e-12:
            raise ValueError("Error: zero or very small derivative.")
        if abs(f) < eps:
            return x0
        x1 = x0 - f / fx
        if abs(x1 - x0) > delta:
            raise ValueError('Error: Divergence')
        if abs(x1 - x0) <= eps * abs(x1):
            return x1
        x0 = x1
    raise ValueError('Error: Maximum Number of Iterations')


# Example function
def example_function(x):
    f = x**2 - 1
    fx = 2 * x
    return f, fx


if __name__ == '__main__':
    # Example usage
    root = newtonRaphson(example_function, 1.5)
    print("The found root is", root)
