import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print('Using backend: ' + matplotlib.get_backend())

def one_array_hardcoded():
    """
    only passing 1 array for y values,
    x values will simply be the index of each point in the array
    """
    y_vals = [0, 1, 3, 5, 4, 2]
    plt.plot(y_vals)
    plt.show()


def two_array_hardcoded():
    x_vals = [5, 3, 2, 3, 5]
    y_vals = [0, 2, 4, 6, 8]
    plt.plot(x_vals, y_vals)
    plt.show()

def linear():
    # simple linear
    slope = m = 2
    y_intercept = b = 5
    x_vals = np.arange(0.0, 2.0, 0.01)
    y_vals = m * x_vals + b
    plt.plot(x_vals, y_vals)
    plt.show()


#one_array_hardcoded()
#two_array_hardcoded()
linear()
