import pg3d.MatrixMath.matrix as mm
import math as m


class Point():
    def __init__(self, app, coordinate, vertex=False):
        self.coordinate = mm.Matrix([coordinate])
        self.app = app
        self.world = app.world
        if not vertex:
            self.world.add_point(self)


    def __repr__(self):
        """
        Defines the behaviour of printing Point objects
        """
        return str(self.coordinate[0])


    def __setitem__(self, index, value):
        """
        Defines the behaviour of setting an indexed Point object to a value
        """
        self.coordinate[0][index] = value


    def __getitem__(self, item):
        """
        Defines the behaviour for indexing a Point object
        """
        if item == 0 or item == 1 or item == 2 or item == 3:
            return self.coordinate[0][item]

        else:
            return "invalid position"

    
    def project(self, P, V):
        """
        Projects the point so that it can be drawn on a 2D screen
        if the point is infront of the camera, the method returns the x, y coordinates of the point
        if the point is behind the camrea it returs False
        """
        point = mm.copy_matrix(self.coordinate.matrix)
       # print(point)
        rotated = point * V
       # print(V)
        projected = rotated * P
       # print(projected)

        if not projected[0][3] <= 0:
            x = (projected[0][0] / projected[0][3]) + self.app.H_WIDTH
            y = (projected[0][1] / projected[0][3]) + self.app.H_HEIGHT
            return x, y

        else:
            return False