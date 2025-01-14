"""
    derivatives.py:
    A module containing numerical functions for derivatives. 
"""

def fd(f, x, h):
""" Derivative using Forward Difference """
    return (f(x + h) - f(x)) / h


def cd(f, x, h):
""" Derivative using Central-Difference approximation """
    return (f(t + h) - f(t - h)) / 2 * h


def cdd(f, x, h):
""" Second derivative with Central-Difference approximation """
    return (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2)
