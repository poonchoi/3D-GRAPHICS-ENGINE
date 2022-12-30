from pygame3D.MatrixMath.matrix import Matrix
import math as m



class Point():
    def __init__(self, app, coordinate, vertex=False):
        self.coordinate = Matrix([coordinate])
        if not vertex:
            app.add_point(self)
        self.app = app
        self.world = app.world


    def __repr__(self):
        return str(self.coordinate[0])


    def __setitem__(self, index, value):
        self.coordinate[0][index] = value


    def __getitem__(self, item):
        if item == 0 or item == 1 or item == 2:
            return self.coordinate[0][item]

        else:
            return "invalid"

    
    def project(self, P, V):
        projected = P * V.inverse() * self.coordinate

        if not projected[0][3] <= 0:
            x = (projected[0][0] / projected[0][3]) + self.app.H_WIDTH
            y = (projected[0][1] / projected[0][3]) + self.app.H_HEIGHT
            return x, y

        else:
            return None