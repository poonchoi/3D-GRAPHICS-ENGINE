import numpy as np

w, h = 1920, 1080
a = w / h
fov = np.pi / 2

znear = 0.1
zfar = 100

M = np.matrix([
    [1/(a*np.tan(fov/2)), 0, 0, 0],
    [0, 1/(np.tan(fov/2)), 0, 0],
    [0, 0, -(znear+zfar)/(zfar-znear), -1],
    [0, 0, -(2*zfar*znear)/(zfar-znear), 0]
])

point = np.array([1, 1, 5, 1])
point = point @ M
proj = np.array([None, None])
# proj[0] = point[0][0] / point[0][3]
# proj[1] = point[0][1] / point[0][3]

print(point[1])
print(proj)