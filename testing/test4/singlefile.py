import math
import numpy as np

def project(point):
    w, h = 1920, 1080
    zfar = 10
    znear = 1
    fov = 60
    a = w / h
    f = 1/math.tan(fov/2)
    q = zfar/(zfar-znear)
    p = np.matrix([
        [a*f,0,0,0],
        [0,f,0,0],
        [0,0,q,1],
        [0,0,-znear*q,0]
    ])

    point = np.array(point)
    projected = np.matmul(p, point.reshape(4,1))
    projected = projected.tolist()
    projected[0][0] = projected[0][0] / projected[3][0]
    projected[1][0] = projected[1][0] / projected[3][0]
    projected[2][0] = projected[2][0] / projected[3][0]
    projected = [projected[0][0], projected[1][0], projected[2][0]]
    projected[0] *= w
    projected[1] *= h
    return projected


p = [1,1,1,1]
print(project(p))