"""
Matrix and Vector math
"""


# Matrix * Vector translation for a 3D point
class Vertex3d(object):
    """Represents a point of 3D geometry"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        w = 1  # w as 1 means this is a position, not direction
        self.trans_vector = np.array([
            [x],
            [y],
            [z],
            [w]
        ])

# http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/
vertex = Vertex3d(10, 10, 10)

trans_x, trans_y, trans_z = (10, 0, 0)
translation_matrix = np.array([
    [1, 0, 0, trans_x],
    [0, 1, 0, trans_y],
    [0, 0, 1, trans_z],
    [0, 0, 0, 1]
])

expected = np.array([
    [20],
    [10],
    [10],
    [1],
])

# order matters: Matrix * Vector
# must use `dot` in numpy, not `*` operator
compare = (np.dot(translation_matrix, vertex.trans_vector)) == expected
assert compare.all()
