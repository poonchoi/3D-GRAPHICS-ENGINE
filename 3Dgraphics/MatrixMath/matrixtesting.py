import matrix as m

a = m.Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

b = m.Matrix([
    [1.23],
    [2.32],
    [3.12]
])

c = m.Matrix([[1.0, 2.0, 3.0]])

print(a*c)
