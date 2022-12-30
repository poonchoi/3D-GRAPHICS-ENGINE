import pg3d

app = pg3d.App([800, 800])

points = [[100, 100, 100], [-100, 100, 100], [-100, -100, 100], [100, -100, 100],
        [100, 100, -100], [-100, 100, -100], [-100, -100, -100], [100, -100, -100]]

for point in points:
    pg3d.Point(app, point)

if __name__ == "__main__":
    app.run()