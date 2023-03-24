from pg3dFINAL import *

app = pg3d.App(bg_color=(40), line_color=(110, 110, 4))

points = [[1, 1, 1], [-1, -1, 1], [-1, 1, 1], [1, -1, 1], 
          [1, 1, -1], [-1, -1, -1], [-1, 1, -1], [1, -1, -1]]

indices = [
    # Front face
    [0, 1, 2],  # First triangle
    [2, 3, 0],  # Second triangle
    # Right face
    [1, 5, 6],  # First triangle
    [6, 2, 1],  # Second triangle
    # Back face
    [5, 4, 7],  # First triangle
    [7, 6, 5],  # Second triangle
    # Left face
    [4, 0, 3],  # First triangle
    [3, 7, 4],  # Second triangle
    # Top face
    [3, 2, 6],  # First triangle
    [6, 7, 3],  # Second triangle
    # Bottom face
    [4, 5, 1],  # First triangle
    [1, 0, 4] # Second triangle
]

classpoints = [pg3d.Point(app, i) for i in points]

for point in points:
    for tri in indices:
        print(points[tri[0]], points[tri[1]], points[tri[2]])
        pg3d.Triangle(app, point[tri[0]], point[tri[1]], point[tri[2]])


app.run()