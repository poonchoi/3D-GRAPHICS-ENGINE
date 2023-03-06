#from pg3d import *
from pg3drestart import *

new_app = pg3d.App([800,800])

cubes = [
    # Front face
    [[-100, -100,  1.0, 1.0],  # Bottom left
    [ 100, -100,  1.0, 1.0],  # Bottom right
    [ 100,  100,  1.0, 1.0],  # Top right
    [-100,  100,  1.0, 1.0],  # Top left
    # Back face
    [-100, -100, -1.0, 1.0],  # Bottom left
    [ 100, -100, -1.0, 1.0],  # Bottom right
    [ 100,  100, -1.0, 1.0],  # Top right
    [-100,  100, -1.0, 1.0]],  # Top left


    # Front face
    [[-100, -100,  4.0, 1.0],  # Bottom left
    [ 100, -100,  4.0, 1.0],  # Bottom right
    [ 100,  100,  4.0, 1.0],  # Top right
    [-100,  100,  4.0, 1.0],  # Top left
    # Back face
    [-100, -100, 2.0, 1.0],  # Bottom left
    [ 100, -100, 2.0, 1.0],  # Bottom right
    [ 100,  100, 2.0, 1.0],  # Top right
    [-100,  100, 2.0, 1.0]],  # Top left


    # Front face
    [[200, -100,  1.0, 1.0],  # Bottom left
    [ 400, -100,  1.0, 1.0],  # Bottom right
    [ 400,  100,  1.0, 1.0],  # Top right
    [200,  100,  1.0, 1.0],  # Top left
    # Back face
    [200, -100, -1.0, 1.0],  # Bottom left
    [ 400, -100, -1.0, 1.0],  # Bottom right
    [ 400,  100, -1.0, 1.0],  # Top right
    [200,  100, -1.0, 1.0]],  # Top left


    # Front face
    [[200, -100,  4.0, 1.0],  # Bottom left
    [ 400, -100,  4.0, 1.0],  # Bottom right
    [ 400,  100,  4.0, 1.0],  # Top right
    [200,  100,  4.0, 1.0],  # Top left
    # Back face
    [200, -100, 2.0, 1.0],  # Bottom left
    [ 400, -100, 2.0, 1.0],  # Bottom right
    [ 400,  100, 2.0, 1.0],  # Top right
    [200,  100, 2.0, 1.0]]  # Top left
]

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


cubes = [
    # Front face
    [[-100, -100,  5.0, 1.0],  # Bottom left
    [ 100, -100,  5.0, 1.0],  # Bottom right
    [ 100,  100,  5.0, 1.0],  # Top right
    [-100,  100,  5.0, 1.0],  # Top left
    # Back face
    [-100, -100, 3.0, 1.0],  # Bottom left
    [ 100, -100, 3.0, 1.0],  # Bottom right
    [ 100,  100, 3.0, 1.0],  # Top right
    [-100,  100, 3.0, 1.0]]  # Top left
]

# for cube in cubes:
#     for tri in indices:
#         pg3d.Triangle(new_app, cube[tri[0]], cube[tri[1]], cube[tri[2]])

for cube in cubes:
    for point in cube:
        pg3d.Point(new_app, point)

if __name__ == "__main__":
    new_app.run()