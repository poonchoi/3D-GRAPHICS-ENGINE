import pygame as pg
import math as m
from MatrixMath import matrix as mm
from matrices import *
import time as t

class Camera:
    def __init__(self, app, position):
        self.app = app
        pg.mouse.set_visible(1)

        self.pos = mm.Matrix([[*position, 1]])
        self.forward = mm.Matrix([[0, 0, 1, 1]])
        self.up = mm.Matrix([[0, 1, 0, 1]])
        self.right = mm.Matrix([[1, 0, 0, 1]])

        self.speed = 1
        self.angle = m.radians(1)

    def yaw(self, angle):
        self.up *= rotate_y(angle)
        self.forward *= rotate_y(angle)
        self.right *= rotate_y(angle)

    def pitch(self, angle):
        self.up *= rotate_x(angle)
        self.forward *= rotate_x(angle)
        self.right *= rotate_x(angle)

    def rot_mat(self):
        fx, fy, fz, fw = self.forward[0]
        rx, ry, rz, rw = self.right[0]
        ux, uy, uz, uw = self.up[0]

        return mm.Matrix([[rx, ux, fx, 0],
                          [ry, uy, fy, 0],
                          [rz, uz, fz, 0],
                          [ 0,  0,  0, 1]])
    
    def trans_mat(self):
        x, y, z, w = self.pos[0]

        return mm.Matrix([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [-x,-y,-z,1]])
    
    def cam_mat(self):
        return self.trans_mat() * self.rot_mat()

    def movement(self):
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.right = self.speed * self.right
            self.pos = self.pos - self.right
        if key[pg.K_d]:
            self.right = self.speed * self.right
            self.pos = self.pos + self.right
        if key[pg.K_w]:
            self.forward = self.speed * self.forward
            self.pos = self.pos + self.forward
        if key[pg.K_s]:
            self.forward = self.speed * self.forward
            self.pos = self.pos - self.forward

        if key[pg.K_LEFT]:
            self.yaw(-self.angle)
        if key[pg.K_RIGHT]:
            self.yaw(self.angle)
        if key[pg.K_UP]:
            self.pitch(-self.angle)
        if key[pg.K_DOWN]:
            self.pitch(self.angle)

        
        x, y = pg.mouse.get_pos()
        # self.yaw((x - self.app.hwidth)/1000)
        # self.pitch((y - self.app.hheight)/1000)
        #print((x - self.app.hwidth)/1000, (y - self.app.hheight)*-1/1000)
        print(x, y)
        #pg.mouse.set_pos((self.app.hwidth, self.app.hheight))
        


class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 600, 600
        self.hwidth, self.hheight = self.width / 2, self.height / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        self.cam = Camera(self, [0, 0, 0])

        # vertices of cube
        self.points = [mm.Matrix([[100, 100, 1, 1]]),mm.Matrix([[100, -100, 1, 1]]),mm.Matrix([[-100, -100, 1, 1]]),mm.Matrix([[-100, 100, 1, 1]]),
                       mm.Matrix([[100, 100, 20, 1]]),mm.Matrix([[100, -100, 20, 1]]),mm.Matrix([[-100, -100, 20, 1]]),mm.Matrix([[-100, 100, 20, 1]]), mm.Matrix([[0, 0, 0, 1]])]
        #self.points = [mm.Matrix([[0, 100, 3, 1]])]
        self.points = [mm.Matrix([[-1, 1, 3, 1]]), mm.Matrix([[1, -1, 3, 1]]), mm.Matrix([[1, 1, 3, 1]]), mm.Matrix([[-1, -1, 3, 1]]),
                       mm.Matrix([[-1, 1, 5, 1]]), mm.Matrix([[1, -1, 5, 1]]), mm.Matrix([[1, 1, 5, 1]]), mm.Matrix([[-1, -1, 5, 1]])]
        self.fov = 90
        self.f = 1 / m.tan(m.radians(self.fov/2))
        self.zf = 1000
        self.zn = .1
        self.g = self.zf / (self.zf - self.zn)
        self.a = self.height / self.width
        self.angle = m.radians(1)
        
        self.proj = mm.Matrix([[self.a*self.f, 0, 0, 0],
                               [0, self.f, 0, 0],
                               [0, 0, self.g, 1],
                               [0, 0, -self.zn*self.g, 0]])


    def rotx(self, point):
        rotx = mm.Matrix([[1, 0, 0, 0],
                          [0, m.cos(self.angle), -m.sin(self.angle), 0],
                          [0, m.sin(self.angle), m.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        return point * rotx
    
    def roty(self, point):
        roty = mm.Matrix([[m.cos(self.angle), 0, m.sin(self.angle), 0],
                          [0, 1, 0, 0],
                          [-m.sin(self.angle), 0, m.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        return point * roty
    
    def rotz(self, point):
        rotz = mm.Matrix([[m.cos(self.angle), -m.sin(self.angle), 0, 0],
                          [m.sin(self.angle), m.cos(self.angle), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        return point * rotz 
    

    def draw(self):
        self.screen.fill((0))

        for i in range(len(self.points)):
            copy = mm.copy_matrix(self.points[i])
            copy *= self.cam.cam_mat()
            self.project(copy)
            
    
    def project_ortho(self, point):
        pg.draw.circle(self.screen, (0), (point[0][0] + self.hwidth, point[0][1] + self.hheight), 1)


    def project(self, point):
        projected = point * self.proj

        x, y, z, w = projected[0]

        if w != 0:
            x /= w
            y /= w
            z /= w
            # projected[0][3] /= w
            
            if (x < 2 and x > -2) and (y < 2 and y > -2) and not(w < 0):
                x, y = (x + 1) * self.hwidth, (y + 1) * self.hheight
                pg.draw.circle(self.screen, (255,255,255), (x, y), (2))
                #self.screen.set_at((int(x), int(y)), (0))


    def run(self):
        while True:
            pg.mouse.set_pos((self.hwidth, self.hheight))
            self.draw()
            self.cam.movement()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = App()
    app.run()