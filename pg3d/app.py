import pygame as pg
import math as m
from pygame.colordict import THECOLORS
from typing import Optional, Tuple, Sequence
import pg3d.MatrixMath.matrix as mm
from pg3d.camera import Camera
from pg3d.triangle import Triangle


class App:
    def __init__(
        self,
        dimensions=(1000, 700),
        cam_pos=[0, 0, 0],
        BG_COLOR=(0, 0, 0),
        LINE_COLOR=(255, 255, 255),
        VERTEX_SIZE=2,
        stats=False,
        fullscreen=False,
        mouse_look=False,
    ):
        """
        Initialises the library, creates the projection matrix and creates a camera

        Args:
            dimensions ([tuple], optional): [window dimensions]. Defaults to (1000, 700).
            cam_pos ([list], optional): [position of camrea]. Defaults to [0, 0, 0].
            BG_COLOR ([tuple], optional): [background color]. Defaults to (0, 0, 0).
            LINE_COLOR ([tuple], optional): [color for drawing lines and points]. Defaults to (255, 255, 255).
            VERTEX_SIZE ([int], optional): [size of points]. Defaults to 2.
            stats ([bool], optional): [shows some stats on screen]. Defaults to False.
            fullscreen ([bool], optional): [makes screen fullscreen]. Defaults to False.
            mouse_look ([bool], optional): [use mouse movement too look with camera]. Defaults to False.
        """
        pg.init()

        if fullscreen:
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN, vsync=1)
            self.dimensions = (
                self.width,
                self.height,
            ) = pg.display.get_surface().get_size()
        else:
            self.dimensions = self.width, self.height = dimensions
            self.screen = pg.display.set_mode(self.dimensions, pg.RESIZABLE, vsync=1)

        self.half_width, self.half_height = self.width / 2, self.height / 2
        self.FPS: int = 60
        self.screen = pg.display.set_mode(self.dimensions, pg.RESIZABLE, vsync=1)
        self.clock = pg.time.Clock()
        self.stats = stats

        if mouse_look:
            pg.mouse.set_visible(0)
        self.mouse_look = mouse_look

        self.BG_COLOR = BG_COLOR
        self.LINE_COLOR = LINE_COLOR
        self.VERTEX_SIZE = VERTEX_SIZE

        self.camera = Camera(self, cam_pos)

        self.mesh = []

        self.fov = 90
        self.zf = 1000
        self.zn = 0.1

        m00 = (self.height / self.width) * (1 / m.tan(m.radians(self.fov / 2)))
        m11 = 1 / m.tan(m.radians(self.fov / 2))
        m22 = self.zf / (self.zf - self.zn)
        m32 = -self.zn * (self.zf / (self.zf - self.zn))

        self.projection_matrix = mm.Matrix(
            [[m00, 0, 0, 0], [0, m11, 0, 0], [0, 0, m22, 1], [0, 0, m32, 0]]
        )

    def _update_projection_matrix(self):
        """
        Updates the projection matrix when the values of fov and aspect ratio are changed by the user
        """
        m00 = (self.height / self.width) * (1 / m.tan(m.radians(self.fov / 2)))
        m11 = 1 / m.tan(m.radians(self.fov / 2))
        m22 = self.zf / (self.zf - self.zn)
        m32 = -self.zn * (self.zf / (self.zf - self.zn))

        self.projection_matrix = mm.Matrix(
            [[m00, 0, 0, 0], [0, m11, 0, 0], [0, 0, m22, 1], [0, 0, m32, 0]]
        )

    def _add_point(self, point):
        """
        When a user creates a point object this function is called and adds the point to mesh

        Args:
            point ([Point]): [a point object]
        """
        self.mesh.append([point])

    def _add_triangle(self, triangle):
        self.mesh.append(triangle)

    def _draw(self):
        self.screen.fill(self.BG_COLOR)

        for shape in self.mesh:
            if type(shape) == Triangle:
                shape._project()

            else:
                for point in shape:
                    projected = point._project(
                        self.projection_matrix, self.camera._cam_mat()
                    )

                    if projected is not None:
                        x, y, z = projected

                        if point.vertex == True:
                            pg.draw.circle(
                                self.screen, self.LINE_COLOR, (x, y), self.VERTEX_SIZE
                            )

    def _display_stats(self):
        """
        If self.stats is true, this method will display stats on screen every frame
        """
        font = pg.font.Font("freesansbold.ttf", 10)
        fov = font.render(f"fov = {self.fov}", True, (0, 255, 0))
        fps = font.render(f"fps = {round(self.clock.get_fps())}", True, (0, 255, 0))
        dimensions = font.render(f"dimensions = {self.dimensions}", True, (0, 255, 0))
        self.screen.blit(fov, (5, 5))
        self.screen.blit(fps, (5, 15))
        self.screen.blit(dimensions, (5, 25))

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                exit()

            elif event.type == pg.MOUSEWHEEL:
                if event.y == 1:
                    self.fov -= 1
                else:
                    self.fov += 1
                self._update_projection_matrix()

            elif event.type == pg.VIDEORESIZE:
                self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                self.dimensions = self.width, self.height = (event.w, event.h)
                self.half_width, self.half_height = self.width / 2, self.height / 2
                self._update_projection_matrix()

            elif (event.type == pg.MOUSEMOTION) and (self.mouse_look == True):
                self.camera._mouse_look(event.rel)

    def run(self):
        """
        Main loop of the library which checks for camera control and other events, and draws and projects the points
        """
        while True:
            self._draw()
            self.camera._movement()
            self._check_events()
            if self.stats:
                self._display_stats()

            if self.mouse_look == True:
                pg.mouse.set_pos((self.half_width, self.half_height))

            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.update()
            self.clock.tick(self.FPS)
