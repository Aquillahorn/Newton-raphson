def newtonRaphson(g, x0, eps, delta, itermax):
    x = x0  # Initialize the root estimate with the initial guess x0
    for _ in range(itermax):  # Iterate up to the maximum number of iterations
        f, fx = g(x)  # Evaluate the function and its derivative at the current estimate x
        if abs(fx) < delta:  # Check if the derivative is too small (criteria for divergence)
            raise Exception("Error: Divergence")  # Raise an exception if the method is diverging
        step = f / fx  # Calculate the step using Newton-Raphson method
        if abs(step) < eps:  # Check if the step size is smaller than the tolerance
            return x  # Return the root estimate if within tolerance
        x -= step  # Update the root estimate for the next iteration
    raise Exception("Error: Maximum Number of Iterations")  # Raise an exception if maximum iterations exceeded

# Example usage:
# Define your function g(x) and its derivative
def g(x):
    f = x**2 - 4  # Define the function f(x)
    fx = 2*x  # Define the derivative f'(x)
    return f, fx

x0 = 3  # Initial guess
eps = 1e-6  # Tolerance
delta = 1e-6  # Divergence criteria
itermax = 100  # Maximum number of iterations

try:
    root = newtonRaphson(g, x0, eps, delta, itermax)  # Call the newtonRaphson function
    print("Root found:", root)  # Print the root if found within tolerance
except Exception as e:
    print(e)  # Print any exceptions raised during the computation
