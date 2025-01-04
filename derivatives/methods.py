"""
    A module containing numerical functions for derivatives and integrals
"""

"""
    Method 1 - Forward Difference
    We write a function that takes as arguments a function f, 
    a point x where to calculate the derivative and a point h to the right of x.
"""
def fderivative(f, x, h):
    return (f(x + h) - f(x)) / h
