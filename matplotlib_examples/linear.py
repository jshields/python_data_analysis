import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print('Using backend: ' + matplotlib.get_backend())

plt.title('linear')
plt.grid(True)

slope = m = 2
y_intercept = b = 5

plt.text(1, 6, 'y = {slope:.2f}x + {intercept:.2f}'.format(slope=slope, intercept=y_intercept))

x_vals = np.arange(0.0, 2.0, 0.01)
y_vals = m * x_vals + b

plt.plot(x_vals, y_vals)
plt.show()
