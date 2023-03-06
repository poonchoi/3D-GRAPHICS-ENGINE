import pg3d.MatrixMath.matrix as mm
import math as m
from pg3dmarch.matrices import *


def rotate_x(angle):
    return mm.Matrix([[1, 0, 0, 0],
                      [0, m.cos(angle), m.sin(angle), 0],
                      [0, -m.sin(angle), m.cos(angle), 0],
                      [0, 0, 0, 1]])


def rotate_y(angle):
    return mm.Matrix([[m.cos(angle), 0, -m.sin(angle), 0],
                      [0, 1, 0, 0],
                      [m.sin(angle), 0, m.cos(angle), 0],
                      [0, 0, 0, 1]])


def rotate_z(angle):
    return mm.Matrix([[m.cos(angle), m.sin(angle), 0, 0],
                      [-m.sin(angle), m.cos(angle), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])