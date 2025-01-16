"""
    Here we test the integration methods defined in integrals.py.
"""

import numpy as np
import matplotlib.pyplot as plt
import integrals as itg


# First we need a function to integrate:
def f(x):
    return x ** 2 * np.cos(x)

# Let's also define its indefinite integral analytically, suppose C = 0
def intf(x):
    return x ** 2 * np.sin(x) -2 * (-x * np.cos(x) + np.sin(x))


# Let's plot them both to see how they look:
x_axis = np.arange(-10, 10, 0.1)
y_axis = [f(i) for i in x_axis]

plt.figure(figsize=(10,5), dpi=150)
plt.subplot(121)
plt.plot(x_axis, y_axis, label=r"$f(x)=x^2cos(x)$")
plt.title("Graph of f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

y_axis_2 = [intf(i) for i in x_axis]
plt.subplot(122)
plt.plot(x_axis, y_axis_2, label=r"$\int f(x) dx$", color="orange")
plt.title("Graph of the Integral of f(x)")
plt.xlabel("x")                                                                  
plt.ylabel("f'(x)")
plt.legend()
plt.show()


# Let's calculate the integral from 0 to 15 using the analytical integral
# we implemented above, then compare the result with the other methods.
# dintf = definite integral of f
a = 0 
b = 15

def dintf(f, a, b):
    return f(b) - f(a)

area = dintf(intf, a, b)
print(f'Analytical answer = {area}\n')                


# Now let's see what we get by using different methods. Let's use an array
# of values for N so we can better appreciate what happens depending on the
# number of slices in [a,b].
N = np.arange(1,3001) 

def print_integral(g, f, a, b, N):
    integrals = [g(f, a, b, n) for n in N]
    for i, n in zip(integrals, N):
	# We don't need to print thousands of lines
        if n % 100 == 0:
            print(f'N = {n:4}, {i}')	    

print('Simple Integration:')
print_integral(itg.sint, f, a, b, N)

print('\nTrapezoid Rule:')
print_integral(itg.tint, f, a, b, N)

print("\nSimpson's Rule")
# Simpson's integral requires an even number N
M = [i for i in range(2, 3001, 2)]
print_integral(itg.simp, f, a, b, M)











