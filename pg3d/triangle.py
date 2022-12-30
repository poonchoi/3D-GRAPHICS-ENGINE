from pg3d.point import Point
import pygame as pg

class Triangle:
    def __init__(self, app, a, b, c):
        self.points = [Point(app, a, True), Point(app, b, True), Point(app, c, True)]
        self.projected_points = [None for i in range(3)]
        self.app = app
        app.add_triangle(self)

    def connect_points(self):
        pg.draw.polygon(self.app.screen, (255,255,255), self.projected_points, 1)

    def check_projected(self):
        check = True
        for i in range(3):
            if self.projected_points[i] == False:
                check = False
        return check
    
    def __getitem__(self, index):
        return self.points[index]