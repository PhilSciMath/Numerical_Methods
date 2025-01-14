"""
    integrals.py:
    Here we define some functions for integrals using numerical methods.
    As with derivatives, delta x cannot go to infinity, so we must use a 
    limited value, which in most cases is h = (b - a) / N. The numerator 
    indicates the interval of integration and the N in the denominator says 
    how many rectangles we want that interval divided into.
"""


def sint(f, a, b, N):
""" Integration by Riemann Sum """
    h = (b - a) / N
    return sum(f(a + i * h) * h for i in range(N))


def tint(f, a, b, N):
""" Integration by the Trapezoid Rule """
    h = (b - a) / N
    value = sum(f(a + i * h) for i in range(1, N))
    return (f(a) + f(b) + 2 * value) * h / 2


def simp(f, a, b, N):
""" Integration by Simpson's Rule """
    if N % 2 != 0:
        raise ValueError("N must be even.")

    h = (b - a) / N
    odds = sum(4 * f(a + (2 * i - 1) * h) for i in range(1, N // 2 + 1))
    evens = sum(2 * f(a + 2 * i * h) for i in range(1, N // 2))
    return (f(a) + f(b) + odds + evens) * h / 3
