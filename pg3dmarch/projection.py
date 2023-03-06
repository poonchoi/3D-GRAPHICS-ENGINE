import pg3dmarch.MatrixMath.matrix as mm
import math as m

class Projection():
    def __init__(self, app):
        right = m.tan(app.camera.h_fov / 2)
        left = -right
        top = m.tan(app.camera.v_fov / 2)
        bottom = -top
        far = app.camera.far
        near = app.camera.near

        m00 = 2 / (right - left)
        m11 = 2 / (top - bottom)
        m22 = (far + near) / (far - near)
        m32 = (-2 * far * near) / (far - near)

        self.projection_matrix = mm.Matrix([[m00, 0, 0, 0],
                                            [0, m11, 0, 0],
                                            [0, 0, m22, 1],
                                            [0, 0, m32, 0]])

