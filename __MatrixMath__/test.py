import matrix as mm
import numpy as np
a = mm.Matrix([
    [1,0,0,-5],
    [0,1,0,2],
    [0,0,1,3],
    [0,0,0,1]
])

b = mm.Matrix([[3,4,1,1]])

# a = mm.Matrix([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]])

# b =mm.Matrix([
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]])




print(b)
b = mm.copy_matrix(a)
print(b)