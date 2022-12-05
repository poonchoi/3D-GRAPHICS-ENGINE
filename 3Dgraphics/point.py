from MatrixMath.matrix import Matrix
from world import World
import math as m

class Point(World):
    projection_matrix = Matrix([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 0]])
    def __init__(self, world, coordinate):
        self.coordinate = Matrix([coordinate])
        world.add_point()
    
    def project(self):
        return self.coordinate * Point.projection_matrix

    def __repr__(self):
        return str(self.coordinate[0])

xyz = Point([1, 2, 3])