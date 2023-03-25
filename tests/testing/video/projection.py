import numpy as np
import math as m

class Projection:
    def __init__(self, app):
        n = app.camera.near
        f = app.camera.far
        r = m.tan(app.camera.hfov / 2)
        l = -r
        t = m.tan(app.camera.vfov / 2)
        b = -t

        m00 = 2 / (r - l)
        m11 = 2 / (t - b)
        m22 = (f + n) / (f - n)
        m32 = -2 * n * f / (f - n)

        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]])
        
        HW, HH = app.h_width, app.h_height
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]])