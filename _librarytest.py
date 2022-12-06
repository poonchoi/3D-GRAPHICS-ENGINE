from pygame3D import pg3d

new_app = pg3d.App([800, 800])

points = [[100, 100, 100], [-100, 100, 100], [-100, -100, 100], [100, -100, 100],
        [100, 100, -100], [-100, 100, -100], [-100, -100, -100], [100, -100, -100]]

for point in points:
    pg3d.Point(new_app, point)

if __name__ == "__main__":
    new_app.run()