from pygame3D.point import Point
import pygame as pg

class Triangle:
    def __init__(self, app, a, b, c):
        self.points = [Point(app, a, True), Point(app, b, True), Point(app, c, True)]
        self.projected_points = [[None] for i in range(3)]
        self.app = app
        app.add_triangle(self)

    def connect_points(self):
        print(self.projected_points)
        pg.draw.polygon(self.app.screen, (255,255,255), self.projected_points)

    def check_projected(self):
        for i in range(2):
            if None in self.projected_points[i]:
                self.projected_points[i]
                return False
    
    def __getitem__(self, index):
        return self.points[index]