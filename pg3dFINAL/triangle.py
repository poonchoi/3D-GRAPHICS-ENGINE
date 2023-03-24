from pg3dFINAL.point import Point
import pygame as pg

class Triangle:
    def __init__(self, app, a, b, c):
        self.points = [Point(app, a), Point(app, b, True), Point(app, c)]
        self.app = app
        self.app.add_triangle(self)


    def connect_points(self):
        pg.draw.polygon(self.app.screen, 0, self.projected_points, 1)


    def __getitem__(self, index):
        return self.points[index]