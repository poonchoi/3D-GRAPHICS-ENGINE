from MatrixMath.matrix import Matrix
import pygame as pg

class App:
    def __init__(self, dimensions):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = dimensions
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 100
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.world = World(self.RES, self.screen)

    def run(self):
        while True:
            World.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.FPS)


class Point():
    projection_matrix = Matrix([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 0]])
    def __init__(self, app, coordinate):
        self.coordinate = Matrix([coordinate])
        app.world.add_point()
    
    def project(self):
        return self.coordinate * Point.projection_matrix

    def __repr__(self):
        return str(self.coordinate[0])


class World():
    def __init__(self, dimensions, screen):
        self.dimensions = dimensions
        self.screen = screen
        self.all_shapes = []
        self._PROJECT_MATRIX = Matrix([[1, 0, 0],
                                        [0, 1, 0]
                                        [0, 0, 0]])

    def add_point(self, point):
        self.all_shapes.append([point])

    def add_shape(self, shape):
        self.all_shapes.append(shape)

    def project(self, point):
        return point * self._PROJECT_MATRIX

    def rotate_x(self, angle, point):
        rotateX = Matrix([[1, 0, 0],
                          [0, m.cos(angle), m.sin(angle)],
                          [0, -m.sin(angle), m.cos(angle)]])
        return point * rotateX

    def rotate_y(self, angle, point):
        rotateY = Matrix([[m.cos(angle), 0, -m.sin(angle)],
                          [0, 1, 0],
                          [m.sin(angle), 0, m.cos(angle)]])
        return point * rotateY

    def rotate_z(self, angle, point):
        rotateZ = Matrix([[m.cos(angle), m.sin(angle), 0],
                          [-m.sin(angle), m.cos(angle), 0],
                          [0, 0, 1]])
        return point * rotateZ

    def translate(self, new_pos, point):
        x, y, z = new_pos
        translate = Matrix([[x, 0, 0],
                            [0, y, 0],
                            [0, 0, z]])
        return point * translate

    def draw(self):
        projected_points = [[n, n] for n in range(len(self.self.all_shapes))]
        for shape in self.all_shapes:
            for point in shape:
                # projected_points[shape][point] = self.project(point)
                projected = self.project(point)
                x, y, z = projected
                pg.draw.circle(self.screen, (0,255,0), (projected))

    def check_movement(self):
        key = pg.key.get_pressed()

    def run(self):
        pass