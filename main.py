from pg3d import *

new_app = pg3d.App([1000, 800])

vertices = [
    # Front face
    [-100, -100,  1, 1],  # bottom left
    [ 100, -100,  1, 1],  # bottom right
    [ 100,  100,  1, 1],  # top right
    [-100,  100,  1, 1],  # top left
    # Back face
    [-100, -100, -1, 1],  # bottom left
    [ 100, -100, -1, 1],  # bottom right
    [ 100,  100, -1, 1],  # top right
    [-100,  100, -1, 1],  # top left
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
    [1, 0, 4],  # Second triangle
]

for tri in indices:
    pg3d.Triangle(new_app, vertices[tri[0]], vertices[tri[1]], vertices[tri[2]])


if __name__ == "__main__":
    new_app.run()