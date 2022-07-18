import pygame
from colors import *


class Cube():
    def __init__(self, scale=1, pos=(0,0,0)):
        self.points = [[-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1], [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1]]
        self.pos = self.tx, self.ty, self.tz = pos
        self.scale = scale
    
    def connect_points(self, i, j, points):
        pygame.draw.line(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))