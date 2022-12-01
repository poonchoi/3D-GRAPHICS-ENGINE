import matrix as m

a = m.Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

b = m.Matrix([
    [1],
    [2],
    [3]
])

c = m.Matrix([[1, 2, 3]])

print(a*b)