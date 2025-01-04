"""
    Main
"""
import methods as mtd
import matplotlib.pyplot as plt
import numpy as np

# Defining our function:
def f(x):
    return np.sin(x**2) * np.exp(x/3) / np.sqrt(x**2 + 4)

# Lets take a look at this function's graph.
x_axis = np.arange(1, 10, 0.01)
y_axis = [f(x) for x in x_axis]

plt.plot(x_axis, y_axis, label="f(x)")
plt.title("f(x) versus x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
#plt.show()

# We are going to create an array of values for h, then plot the results, x=3.
# The idea is to see what happens as h gets smaller (approaches 0).
x = 3
h_array = np.logspace(0, -16, num=17, base=10)
df_array = [mtd.fderivative(f, x, h) for h in h_array]

plt.semilogx(h_array, df_array, label="f'(x)", color='orange')
plt.title("Forward Difference")
plt.xlabel("h")
plt.xlim(h_array[-1], h_array[0])
plt.ylabel("f'(x)")
plt.legend()
plt.show()


