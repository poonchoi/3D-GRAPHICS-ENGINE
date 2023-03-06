import pygame as pg
import MatrixMath.matrix as mm
from matrices import *
import math as m

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 600, 600
        self.hwidth, self.hheight = self.height // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.cam = Camera(self.res)

    def proj_mat(self):
        r = m.tan(self.cam.hfov / 2)
        l = -r
        t = m.tan(self.cam.vfov / 2)
        b = -t
        f = self.cam.far
        n = self.cam.near

        m00 = 2 / (r - l)
        m11 = 2 / (t - b)
        m22 = (f + n) / (f - n)
        m32 = (-2 * f * n) / (f - n)

        return mm.Matrix([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]])

    def screen_proj(self, point):
        pointI = point * self.cam.cam_mat()
        print(pointI)
        pointII = pointI * self.proj_mat()
        print(pointII)
        x, y, z, w = pointII[0]

        if not(w > 2 or w < -2 or w == 0):
            x /= w
            y /= w
            z /= w
            print(x, y, z)
            return [x, y, z]
        else:
            return None

    def draw(self):
        self.screen.fill((255, 255, 255))
        points = [mm.Matrix([[0, 0, -3, 1]])]
        
        for point in points:
            proj = self.screen_proj(point)
            if proj != None:
                pg.draw.circle(self.screen, (0, 0, 0), (proj[0]+self.hwidth, proj[1]+self.hheight), 5)


    def run(self):
        while True:
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)


class Camera():
    def __init__(self, res):
        self.pos = mm.Matrix([[0, 0, 0, 1]])
        self.forward = mm.Matrix([[0, 0, 1, 1]])
        self.up = mm.Matrix([[0, 1, 0, 1]])
        self.right = mm.Matrix([[1, 0, 0, 1]])
        self.hfov = 60
        self.a = res[1] / res[0]
        self.vfov = self.hfov * self.a
        self.near = 0.1
        self.far = 100
        self.speed = 1
        self.angle = [0, 0]
        self.aspeed = 0.1
    
    def cam_trans(self):
        x, y, z, w = self.pos[0]
        return mm.Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x,-y,-z,1]])
    
    def rot_mat(self):
        # self.forward *= rotate_x(0.001)
        # self.up *= rotate_x(0.001)
        # self.right *= rotate_x(0.001)
        # self.forward *= rotate_y(-0.001)
        # self.up *= rotate_y(-0.001)
        # self.right *= rotate_y(-0.001)

        fx, fy, fz, fw = self.forward[0]
        ux, uy, uz, uw = self.up[0]
        rx, ry, rz, rw = self.right[0]
        return mm.Matrix([
            [rx,ux,fx,0],
            [ry,uy,fy,0],
            [rz,uz,fz,0],
            [0, 0, 0, 1]])
    
    def cam_mat(self):
        return self.cam_trans() * self.rot_mat()


if __name__ == "__main__":
    app = App()
    app.run()