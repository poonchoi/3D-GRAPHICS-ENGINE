import pg3d.MatrixMath.matrix as mm
import math as m


def rotate_x(angle):
    """
    Rotation matrix on x-axis

    Args:
        angle ([float]): [Angle for rotation]

    Returns:
        [Matrix]: [Creates rotation matrix along x-axis]
    """
    return mm.Matrix(
        [
            [1, 0, 0, 0],
            [0, m.cos(angle), m.sin(angle), 0],
            [0, -m.sin(angle), m.cos(angle), 0],
            [0, 0, 0, 1],
        ]
    )


def rotate_y(angle):
    """
    Rotation matrix on y-axis

    Args:
        angle ([float]): [Angle for rotation]

    Returns:
        [Matrix]: [Creates rotation matrix along y-axis]
    """
    return mm.Matrix(
        [
            [m.cos(angle), 0, -m.sin(angle), 0],
            [0, 1, 0, 0],
            [m.sin(angle), 0, m.cos(angle), 0],
            [0, 0, 0, 1],
        ]
    )


def rotate_z(angle):
    """
    Rotation matrix on z-axis

    Args:
        angle ([float]): [Angle for rotation]

    Returns:
        [Matrix]: [Creates rotation matrix along z-axis]
    """
    return mm.Matrix(
        [
            [m.cos(angle), m.sin(angle), 0, 0],
            [-m.sin(angle), m.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
