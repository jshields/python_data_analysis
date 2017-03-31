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



def quadratic_roots(a, b, c):
    """
    use the quadratic formula to find roots, x values at y = 0
    a*x^2 + b*x + c = 0
    """
    # "plus" of "plus or minus"
    x1 = -b + sqrt(b ^ 2 - 4*a*c) / 2*a

    # "minus" of "plus or minus"
    x2 = -b - sqrt(b ^ 2 - 4*a*c) / 2*a

    return x1, x2


def quadratic():
    """a*x^2 + b*x + c = y"""
    a = 2
    b = 3
    c = 4
    x_vals = np.arange(0.0, 2.0, 0.01)
    y_vals = a*x_vals^2 + b*x_vals + c

    root_x1, root_x2 = quadratic_roots(a, b, c)
    roots_y = 0

    plt.text(root_x1 - 0.08, roots_y, "root 1", ha="right", weight="heavy")
    plt.text(root_x1, roots_y, "x = %0.2f\ny = %0.2f"%(root_x1, roots_y), rotation=0, color='gray')

    plt.text(root_x2 - 0.08, roots_y, "root 2", ha="right", weight="heavy")
    plt.text(root_x2, roots_y, "x = %0.2f\ny = %0.2f"%(root_x2, roots_y), rotation=0, color='gray')

    plt.plot(root_x1, roots_y, "ro")
    plt.plot(root_x2, roots_y, "ro")

    plt.plot(x_vals, y_vals)


#one_array_hardcoded()
#two_array_hardcoded()
