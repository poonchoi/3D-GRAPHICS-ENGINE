import pygame as pg
import math as m

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 600, 600
        self.hwidth, self.hheight = self.height // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        self.points = [[100, 100, 5],[100, -100, 5],[-100, -100, 5],[-100, 100, 5],
                       [100, 100, 10],[100, -100, 10],[-100, -100, 10],[-100, 100, 10]]
        # self.points = [[100,0,10],[100,0,1]]
        self.fov = m.pi / 3
        self.f = 1 / m.tan(self.fov/2)
        self.zf = 10
        self.zn = 1
        self.g = self.zf / (self.zf - self.zn)
        self.a = self.height / self.width

    def draw(self):
        self.screen.fill((255, 255, 255))
        for point in self.points:
            x, y = self.project(point)
            pg.draw.circle(self.screen, (0), (x+self.hwidth, y+self.hheight), 4)

    def project(self, point):
        x = point[0]
        y = point[1]
        z = point[2]

        x *= (self.a * self.fov) / z
        y *= self.fov / z
        
        return x, y


    def run(self):
        while True:
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)




if __name__ == "__main__":
    app = App()
    app.run()