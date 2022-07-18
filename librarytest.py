from libraryEngineTest import *


angle = pygame.mouse.get_pos()[0] / 1000
points = [[-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1], [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1]]
projected_points = [[n, n] for n in range(len(points))]
i = 0
for point in points:
    rotated = rotateZ(point, pygame.mouse.get_pos()[1] / 500)
    rotated = rotateY(rotated, pygame.mouse.get_pos()[0] / 500)
    projected = project(rotated)
    x = projected[0][0] * scale + H_WIDTH
    y = projected[1][0] * scale + H_HEIGHT
    projected_points[i] = [x, y]
    pygame.draw.circle(screen, BLACK, (x, y), 5)
    i += 1
    
for p in range(4):
    connect_points(p, (p+1) % 4, projected_points)
    connect_points(p+4, ((p+1) % 4) + 4, projected_points)
    connect_points(p, (p+4), projected_points)


if __name__ == '__main__':
    app = App()
    app.run()