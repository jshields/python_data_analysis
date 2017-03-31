"""
Basic examples of numpy
"""
import numpy as np

np.array([0, 1, 2, 3, 4])


# 8 bytes per 64 bit integer
print(
    'data type: ', np.dtype,
    'size: ', np.itemsize
)

two_by_two_np_array = np.arange(4).reshape(2, 2)

cast_py_list = [list(arr) for arr in list(two_by_two_np_array)]

assert cast_py_list == [[0, 1],[2, 3]]

comparison = cast_py_list == two_by_two_np_array


# all elements match between Python list and NumPy array comparison
assert comparison.all()

try:
    # trying to compare this way won't work
    bool(comparison)
except ValueError as ex:
    print(ex)
