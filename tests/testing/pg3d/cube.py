from pg3d.point import Point
from pg3d.triangle import Triangle


class Cube:
    def __init__(self, app, centre, l):
        """
        __init__ method used to define coordinates of cube 
        and coordinates of triangles.

        Then triangles of the cube are made using the triangle class.
        """
        x, y, z = centre

        # creates the 8 vertices of the cube
        self.points = [
            [x + l/2, y + l/2, z + l/2],
            [x + l/2, y + l/2, z - l/2],
            [x + l/2, y - l/2, z + l/2],
            [x + l/2, y - l/2, z - l/2],
            [x - l/2, y + l/2, z + l/2],
            [x - l/2, y + l/2, z - l/2],
            [x - l/2, y - l/2, z + l/2],
            [x - l/2, y - l/2, z - l/2]]

        # defines the indices of the points to make each triangle
        self.triangle_indices = [
            [0, 1, 2], [2, 1, 3]
            [4, 5, 6], [6, 5, 7]
            [0, 4, 1], [1, 4, 5]
            [2, 6, 3], [3, 6, 7]
            [0, 2, 4], [4, 2, 6]
            [1, 5, 3], [3, 5, 7]]
        
        # creates all the triangles in the cube
        self.triangles = [Triangle(app, self.points[triangle[0]], self.points[triangle[1]], self.points[triangle[2]]) for triangle in self.triangle_indices]