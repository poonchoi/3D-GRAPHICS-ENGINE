import numpy as np
import pygame as pg


def projection_matrix(n, f, fov, a):
    fov_rad = np.deg2rad(fov)
    t = np.tan(fov_rad / 2) * n
    b = -t
    r = t * a
    l = -r
    return np.array([
        [(2*n)/(r-l), 0, (r+l)/(r-l), 0],
        [0, (2*n)/(t-b), (t+b)/(t-b), 0],
        [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
        [0, 0, 1, 0]])


def view_matrix(camera, x, y):
    y_rot = np.array([
        [np.cos(y), 0, np.sin(y)],
        [0, 1, 0],
        [-np.sin(y), 0, np.cos(y)]])

    x_rot = np.array([
        [1, 0, 0],
        [0, np.cos(x), -np.sin(x)],
        [0, np.sin(x), np.cos(x)]])

    o = x_rot @ y_rot

    R00, R01, R02 = o[0,:]
    R10, R11, R12 = o[1,:]
    R20, R21, R22 = o[2,:]

    x, y, z = camera

    return np.array([
        [R00, R01, R02, -x],
        [R10, R11, R12, -y],
        [R20, R21, R22, -z],
        [0, 0, 0, 1]])


def perspective_projection(point, projection_matrix, view_matrix):
    cam_point = np.linalg.inv(view_matrix) @ point
    projected_vertices = projection_matrix @ cam_point
    x = projected_vertices[0] / projected_vertices[3]
    y = projected_vertices[1] / projected_vertices[3]

    return x, y


if (__name__ == "__main__"):
    pg.init()
    RES = WIDTH, HEIGHT = 600, 600
    H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
    FPS = 100
    screen = pg.display.set_mode(RES)
    clock = pg.time.Clock()
    screen.fill((255, 255, 255))

    #############################################
    
    points = [[100, 100, 1, 1], [-100, 100, 1, 1], [-100, -100, 1, 1], [100, -100, 1, 1],
            [100, 100, 2, 1], [-100, 100, 2, 1], [-100, -100, 2, 1], [100, -100, 2, 1]]
    camera = [0, 0, 0]
    p = projection_matrix(0.1, 1000, 90, WIDTH/HEIGHT)
    v = view_matrix(camera, 0, 0)

    #############################################

    while True:
        for point in points:
            x, y = perspective_projection(point, p, v)
            pg.draw.circle(screen, (0,0,0), (x+H_WIDTH, y+H_HEIGHT), 2)

        [exit() for i in pg.event.get() if i.type == pg.QUIT]
        pg.display.set_caption(f"{round(clock.get_fps())} FPS")
        pg.display.flip()
        clock.tick(FPS)