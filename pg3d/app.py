import pygame as pg
import math as m
from pygame.colordict import THECOLORS
from typing import Optional, Tuple, Sequence
import pg3d.MatrixMath.matrix as mm
from pg3d.camera import Camera
from pg3d.triangle import Triangle
from pg3d.point import Point


class App:
    def __init__(
        self,
        dimensions=(1000, 700),
        cam_pos=[0, 0, 0],
        BG_COLOR=None,
        LINE_COLOR=None,
        VERTEX_SIZE=2,
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
            self._screen = pg.display.set_mode((0, 0), pg.FULLSCREEN, vsync=1)
            self._dimensions = (
                self._width,
                self._height,
            ) = pg.display.get_surface().get_size()
        else:
            self._dimensions = self._width, self._height = dimensions
            self._screen = pg.display.set_mode(self._dimensions, pg.RESIZABLE, vsync=1)

        self._half_width, self._half_height = self._width / 2, self._height / 2
        self.FPS = 60
        self._screen = pg.display.set_mode(self._dimensions, pg.RESIZABLE, vsync=1)
        self._clock = pg.time.Clock()
        self.stats = False
        self.check_stats = 0

        if mouse_look:
            pg.mouse.set_visible(
                0
            )  # sets the mouse to invisible if mouse movement is turned on

        self.mouse_look = mouse_look

        self.BG_COLOR = BG_COLOR
        self.LINE_COLOR = LINE_COLOR
        self.VERTEX_SIZE = VERTEX_SIZE

        if (self.BG_COLOR is None) and (
            self.LINE_COLOR is not None
        ):  # user inputs line color but not bg color
            self.BG_COLOR = (
                255 - self.LINE_COLOR[0],
                255 - self.LINE_COLOR[1],
                255 - self.LINE_COLOR[2],
            )
        elif (self.BG_COLOR is not None) and (
            self.LINE_COLOR is None
        ):  # user inputs bg color but not line color
            self.LINE_COLOR = (
                255 - self.BG_COLOR[0],
                255 - self.BG_COLOR[1],
                255 - self.BG_COLOR[2],
            )
        else:  # user inputs nothing for bg and line color
            self.BG_COLOR = (0, 0, 0)
            self.LINE_COLOR = (255, 255, 255)

        self.camera = Camera(cam_pos)

        self.mesh = []

        self.fov = 90
        self.z_far = 1000
        self.z_near = 0.1

        m00 = (self._height / self._width) * (1 / m.tan(m.radians(self.fov / 2)))
        m11 = 1 / m.tan(m.radians(self.fov / 2))
        m22 = self.z_far / (self.z_far - self.z_near)
        m32 = -self.z_near * (self.z_far / (self.z_far - self.z_near))

        self.projection_matrix = mm.Matrix(
            [[m00, 0, 0, 0], [0, -m11, 0, 0], [0, 0, m22, 1], [0, 0, m32, 0]]
        )

    def _update_projection_matrix(self):
        """
        Updates the projection matrix when the values of fov and aspect ratio are changed by the user
        """
        m00 = (self._height / self._width) * (1 / m.tan(m.radians(self.fov / 2)))
        m11 = 1 / m.tan(m.radians(self.fov / 2))
        m22 = self.z_far / (self.z_far - self.z_near)
        m32 = -self.z_near * (self.z_far / (self.z_far - self.z_near))

        self.projection_matrix = mm.Matrix(
            [[m00, 0, 0, 0], [0, -m11, 0, 0], [0, 0, m22, 1], [0, 0, m32, 0]]
        )

    def add_point(self, point):
        """
        When a user creates a point object this function is called and adds the point to mesh

        Args:
            point ([Point]): [a point object]
        """
        self.mesh.append(point)

    def add_triangle(self, triangle):
        self.mesh.append(triangle)

    def _draw(self):
        self._screen.fill(self.BG_COLOR)

        for shape in self.mesh:
            if type(shape) == Triangle:
                shape._project()

            elif type(shape) == Point:
                projected = shape._project(
                    self.projection_matrix, self.camera._cam_mat()
                )

                if projected is not None:
                    x, y, z = projected

                    if shape._vertex == True:
                        pg.draw.circle(
                            self._screen, self.LINE_COLOR, (x, y), self.VERTEX_SIZE
                        )

    def display_stats(self):
        """
        If self.stats is true, this method will display stats on screen every frame
        """
        if self.stats == True:
            bg = self.BG_COLOR
            font_color = (255 - bg[0], 255 - bg[1], 255 - bg[2])
            font = pg.font.Font("freesansbold.ttf", 10)
            fov = font.render(f"fov = {self.fov}", True, font_color)
            fps = font.render(f"fps = {round(self._clock.get_fps())}", True, font_color)
            dimensions = font.render(
                f"dimensions = {self._dimensions}", True, font_color
            )
            self._screen.blit(fov, (5, 5))
            self._screen.blit(fps, (5, 15))
            self._screen.blit(dimensions, (5, 25))

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                exit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_o:
                if self.check_stats % 2 == 0:
                    self.stats = True

                else:
                    self.stats = False

                self.check_stats += 1

            elif event.type == pg.MOUSEWHEEL:
                if event.y == 1:
                    self.fov -= 1
                else:
                    self.fov += 1
                self._update_projection_matrix()

            elif event.type == pg.VIDEORESIZE:
                self._screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                self._dimensions = self._width, self._height = (event.w, event.h)
                self._half_width, self._half_height = self._width / 2, self._height / 2
                self._update_projection_matrix()

            elif (self.mouse_look == True) and (event.type == pg.MOUSEMOTION):
                self.camera._mouse_look(event.rel)

    def run(self):
        """
        Main loop of the library which checks for camera control and other events, and draws and projects the points
        """
        while True:
            self._draw()
            self.camera._movement()
            self._check_events()
            self.display_stats()

            if self.mouse_look == True:
                pg.mouse.set_pos((self._half_width, self._half_height))

            pg.display.set_caption(f"{round(self._clock.get_fps())} FPS")
            pg.display.update()
            self._clock.tick(self.FPS)
