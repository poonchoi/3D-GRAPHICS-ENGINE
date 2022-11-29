from MatrixMath import matrix as m
from world_space import World_Space

class Point(World_Space):
    def __init__(self, coordinate):
        self.coordinate = m.Matrix(coordinate)
    


point = Point([1,2,3])