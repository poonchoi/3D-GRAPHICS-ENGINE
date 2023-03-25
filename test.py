from pg3dFINAL import *

app = pg3d.App(bg_color=(40), line_color=(110, 110, 4))

points = [[1, 1, 1], [-1, -1, 1], [-1, 1, 1], [1, -1, 1], 
          [1, 1, -1], [-1, -1, -1], [-1, 1, -1], [1, -1, -1]]
cubes = [[-1, -1,  1],  # Bottom left
    [ 1, -1,  1],  # Bottom right
    [ 1,  1,  1],  # Top right
    [-1,  1,  1],  # Top left
    # Back face
    [-1, -1, -1],  # Bottom left
    [ 1, -1, -1],  # Bottom right
    [ 1,  1, -1],  # Top right
    [-1,  1, -1]],  # Top left

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

# classpoints = [pg3d.Point(app, i) for i in points]


# for tri in indices:
#     pg3d.Triangle(app, cubes[0][tri[0]], cubes[0][tri[1]], cubes[0][tri[2]])

pg3d.Shape(app, "cube", 2, [0,0,6])
pg3d.Shape(app, "pyramid", 4, [-5,2,6])
pg3d.Shape(app, "tetrahedron", 4, [5,2,6])

app.run()