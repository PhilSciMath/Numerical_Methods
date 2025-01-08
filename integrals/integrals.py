"""
    Here we define some functions for integrals using numerical methods.
    As with derivatives, delta x cannot go to infinity, so we must use a 
    limited value, which in most cases is h = (b - a) / N. The numerator 
    indicates the interval of integration and the N in the denominator says 
    how many rectangles we want that interval divided into.
"""

"""
    Method 1 - Simple Integration.
    Four arguments are required: a function f, the limits of integration a and
    b, and the number of rectangles N to subdivide the interval [a,b].
"""
def sint(f, a, b, N):
    h = (b - a) / N
    return sum(f(a + i * h) * h for i in range(N))


"""
    Method 2 - Trapezoid Rule.
    Same arguments as the previous one.
"""
def tint(f, a, b, N):
    h = (b - a) / N
    value = sum(f(a + i * h) for i in range(1, N))
    return (f(a) + f(b) + 2 * value) * h / 2


"""
    Method 3 - Simpson's Rule.
"""
def simp(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("N must be even.")

    h = (b - a) / N
    odds = sum(4 * f(a + (2 * i - 1) * h) for i in range(1, N // 2 + 1))
    evens = sum(2 * f(a + 2 * i * h) for i in range(1, N // 2))
    return (f(a) + f(b) + odds + evens) * h / 3
