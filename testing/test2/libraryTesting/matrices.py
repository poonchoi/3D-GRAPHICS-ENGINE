import numpy as np

def project(self, point):
    p = np.matrix(
        [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]])
    point = np.array(point)
    projected = np.dot(p, point.reshape(3, 1))
    projected = projected.tolist()
    return projected


def rotateX(self, point, angle):
    rotateX = np.matrix(
        [[1, 0, 0],
        [0, np.cos(angle), np.sin(angle)],
        [0, -np.sin(angle), np.cos(angle)]])
    point = np.array(point)
    rotated = np.dot(rotateX, point.reshape(3, 1))
    rotated = rotated.tolist()
    return rotated


def rotateY(self, point, angle):
    rotateY = np.matrix(
        [[np.cos(angle), 0, -np.sin(angle)],
        [0, 1, 0],
        [np.sin(angle), 0, np.cos(angle)]])
    point = np.array(point)
    rotated = np.dot(rotateY, point.reshape(3, 1))
    rotated = rotated.tolist()
    return rotated


def rotateZ(self, x, angle):
    rotateZ = np.matrix(
        [[np.cos(angle), np.sin(angle), 0],
        [-np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]])
    x = np.array(x)
    rotated = np.dot(rotateZ, x.reshape(3, 1))
    rotated = rotated.tolist()
    return rotated