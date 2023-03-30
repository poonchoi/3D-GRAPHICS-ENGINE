from Apg3d.point import Point
import pygame as pg


class Triangle:
    def __init__(self, app, vertices):
        """
        Creates triangle

        Args:
            app ([App]): [Specify App object]
            vertices ([list[list]]): [list with 3 cartesian coordinates]
        """

        if not isinstance(vertices, list) and not isinstance(vertices, tuple):
            raise Exception("vertices must be list or tuple")
        
        if not isinstance(vertices[0], list) and not isinstance(vertices[0], tuple):
            raise Exception("vertices must be 2D list or tuple")
        
        # if len(vertices != 3):
        #     raise Exception("vertices must contain 3 coordinates")
        
        self.points = [
            Point(app, vertices[0], False),
            Point(app, vertices[1], False),
            Point(app, vertices[2], False),
        ]
        self._projected_points = []
        self.app = app
        self.app.add_triangle(self)

    def _project(self):
        """
        Projects triangle
        """
        self.projected_points = []
        for point in self.points:
            projected = point._project(
                self.app.projection_matrix, self.app.camera._cam_mat()
            )
            if projected != None:
                self.projected_points.append(projected)

        self._draw_triangle()

    def _draw_triangle(self):
        """
        Draws triangle
        """
        if len(self.projected_points) == 3:
            a, b, c = self.projected_points
            pg.draw.polygon(
                self.app._screen, self.app.LINE_COLOR, (a[:-1], b[:-1], c[:-1]), 1
            )

    def __getitem__(self, index):
        """
        Args:
            index ([int]): [index of triangle]

        Returns:
            [Point]: [returns point]
        """
        return self.points[index]