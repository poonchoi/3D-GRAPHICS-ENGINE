from pg3dFINAL.point import Point
import pygame as pg

class Triangle:
    def __init__(self, app, a, b, c):
        self.points = [Point(app, a), Point(app, b), Point(app, c)]
        self.projected_points = []
        self.app = app
        self.app.add_triangle(self)
    
    def project(self):
        self.projected_points = []
        for point in self.points:
            projected = point.project(self.app.projection_mat, self.app.camera.cam_mat())
            if projected != None:
                self.projected_points.append(projected)
        
        self.draw_triangle()
    
    def draw_triangle(self):
        if len(self.projected_points) == 3:
            a, b, c = self.projected_points
            pg.draw.polygon(self.app.screen, self.app.line_color, (a[:-1], b[:-1], c[:-1]), 1)


    def connect_points(self):
        pg.draw.polygon(self.app.screen, 0, self.projected_points, 1)

    def __getitem__(self, index):
        return self.points[index]