from MatrixMath import matrix as mm

a = mm.zeroes(4, 4)
b = mm.identity(4)
c = mm.Matrix([[1, 2, 3, 4]])

d = c*a

print(c)
print(a)
print(d)