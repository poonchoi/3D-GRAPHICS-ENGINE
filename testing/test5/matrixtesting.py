import MatrixMath as mm
import math as m

height = 700
width = 1000
fov = m.pi / 3
f = 1 / m.tan(fov/2)
zf = 1000
zn = .1
g = zf / (zf - zn)
a = height / width
angle = 0.01

m00 = a * f
m11 = a * f
m22 = g
m23 = -zn * g

proj = mm.Matrix([[m00, 0, 0, 0],
                  [0, m11, 0, 0],
                  [0, 0, m22, 1],
                  [0, 0, m23, 0]])


p = mm.Matrix([[0, 0, 3, 1]])

print(p*proj)