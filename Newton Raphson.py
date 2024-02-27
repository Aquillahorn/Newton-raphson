import numpy as np

def newtonRaphson(g, x0, eps, delta, itermax):
    x = x0
    for i in range(itermax):
        f, fx = g(x)
        if abs(f) < eps:
            return x
        if abs(fx) < delta:
            raise Exception("Error: Divergence")
        x -= f / fx
    raise Exception("Error: Maximum Number of Iterations")

# Define the function and its derivative
def g(x):
    f = x**2 - 4
    fx = 2*x
    return f, fx

# Initial guess
x0 = 2.5

# Tolerance
eps = 1e-6

# Divergence criteria
delta = 1e10

# Maximum number of iterations
itermax = 100

try:
    root = newtonRaphson(g, x0, eps, delta, itermax)
    print("Root found:", root)
except Exception as e:
    print(e)
