from MatrixMath.matrix import Matrix
import math as m

class Point():
    projection_matrix = Matrix([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 0]])


    def __init__(self, app, coordinate):
        self.coordinate = Matrix([coordinate])
        app.add_point(self)
    

    def project(self):
        new_point = self.coordinate * Point.projection_matrix
        return new_point[0]


    def __repr__(self):
        return str(self.coordinate[0])


    def __getitem__(self, item):
        if item == 0 or item == 1 or item == 2:
            return self.coordinate[0][item]
        else:
            return "invalid"