"""
    A module containing numerical functions for derivatives. 
"""

"""
    Method 1 - Forward Difference.
    The derivative function takes three arguments: a function f to derive,
    a point x on which we want to take the derivative, and a value of h
    which is the smallest delta x we can have.
"""
def fd(f, x, h):
    return (f(x + h) - f(x)) / h


"""
    Method 2 - Central-difference Approximation.
    Same as before, it takes a function, an x value and an h value.
"""
def cd(f, x, h):
    return (f(t + h) - f(t - h)) / 2 * h


"""
    Method 3 - Central-Difference for the Second Derivative. Here we 
    implement the central-difference method for the second derivative 
    because it is better than the forward difference method.
    Same arguments again.
"""
def cdd(f, x, h):
    return (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2)
