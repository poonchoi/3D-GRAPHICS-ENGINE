import pygame as pg
from pg3dmarch.camera import Camera
from pg3dmarch.projection import Projection
import pg3dmarch.MatrixMath.matrix as mm


class App:
    def __init__(self, dimensions):
        """
        creates all necessary pygame variables and instantiates World class
        """
        pg.init()
        self.res = self.width, self.height = dimensions
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        self.camera = Camera(self)
        self.projection = Projection(self)

        self.mesh = [[mm.Matrix([[0,0,0,1]]), mm.Matrix([[50,50,1,1]])]]
        self.projected_mesh = []

    def project(self):
        self.projected_mesh = []

        for shape in self.mesh:
            for point in shape:
                pointI = point * self.camera.camera_matrix() 
                pointII = pointI * self.projection.projection_matrix
                x, y, z, w = pointII[0]

                if not(w > 10 or w < -10 or w == 0):
                    x /= w
                    y /= w
                    z /= w
                    self.projected_mesh.append([x, y, z])
                else:
                    return None

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.project()
        for point in self.projected_mesh:
            pg.draw.circle(self.screen, (0, 0, 0), (point[0]+self.h_width, point[1]+self.h_height), 5)


    def run(self):
        """
        The main loop of the program
        """
        while True:
            self.camera.check_movement()
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)