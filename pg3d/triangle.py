from pg3d.point import Point
import pygame as pg

class Triangle:
    def __init__(self, app, a, b, c):
        self.points = [Point(app, a, True), Point(app, b, True), Point(app, c, True)]
        self.projected_points = [None for i in range(3)]
        self.app = app
        self.world = app.world
        self.world.add_triangle(self)

    def connect_points(self):
        """
        Connect the points of the triangle with lines
        """
        pg.draw.polygon(self.app.screen, 0, self.projected_points, 1)

    def check_projected(self):
        """
        Checks if all the points have been projected to decide if the triangle should be drawn
        Returns True if the triangle can be draw
        Returns False if the triangle can't be drawn
        """
        check = True
        for i in range(3):
            if self.projected_points[i] == False:
                check = False
        return check
    
    def __getitem__(self, index):
        """
        Defines the behaviour of indexing Triangle objects
        """
        return self.points[index]