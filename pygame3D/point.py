from MatrixMath.matrix import Matrix
import math as m

class Point():
    projection_matrix = Matrix([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 0]])
    def __init__(self, app, coordinate):
        self.coordinate = Matrix([coordinate])
        app.world.add_point()
    
    def project(self):
        return self.coordinate * Point.projection_matrix

    def __repr__(self):
        return str(self.coordinate[0])