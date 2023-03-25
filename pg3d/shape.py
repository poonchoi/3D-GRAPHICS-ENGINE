from pg3d.triangle import Triangle

class Shape:
    def __init__(self, app, shape="cube", size=1, center=[0,0,0], width=1):
        self.app = app

        self.center = center
        self.size = size
        self.width = width

        triangles, vertices = None, None

        if shape.lower() == "cube":
            vertices, triangles = self.cube()
        elif shape.lower() == "pyramid":
            vertices, triangles = self.pyramid()
        elif shape.lower() == "tetrahedron":
            vertices, triangles = self.tetrahedron()

        if (triangles != None) and (vertices != None):
            for triangle in triangles:
                Triangle(self.app, [vertices[triangle[0]], vertices[triangle[1]], vertices[triangle[2]]])

    def cube(self):
        x, y, z = self.center
        half_size = self.size / 2

        vertices = [
            [x - half_size, y - half_size, z + half_size],  # Front-bottom-left
            [x + half_size, y - half_size, z + half_size],  # Front-bottom-right
            [x + half_size, y + half_size, z + half_size],  # Front-top-right
            [x - half_size, y + half_size, z + half_size],  # Front-top-left
            [x - half_size, y - half_size, z - half_size],  # Back-bottom-left
            [x + half_size, y - half_size, z - half_size],  # Back-bottom-right
            [x + half_size, y + half_size, z - half_size],  # Back-top-right
            [x - half_size, y + half_size, z - half_size]   # Back-top-left
        ]

        triangles = [
            [0, 1, 2], [0, 2, 3],  # Front face
            [1, 5, 6], [1, 6, 2],  # Right face
            [3, 2, 6], [3, 6, 7],  # Top face
            [4, 5, 1], [4, 1, 0],  # Bottom face
            [4, 0, 3], [4, 3, 7],  # Left face
            [7, 6, 5], [7, 5, 4]   # Back face
        ]

        return vertices, triangles
    

    def pyramid(self):
        x, y, z = self.center
        half_size = self.size / 2
        height = self.size

        vertices = [
            [x - half_size, y + half_size, z - half_size], # Bottom-back-left
            [x - half_size, y + half_size, z + half_size], # Bottom-front-left
            [x + half_size, y + half_size, z - half_size], # Bottom-back-right
            [x + half_size, y + half_size, z + half_size], # Bottom-front-right
            [x, y - half_size, z] # Top
        ]

        triangles = [
            [0, 1, 2], [0, 2, 3], [1,2,3],  # Base face
            [0, 4, 3],  # Front-left face
            [1, 4, 0],  # Front-right face
            [2, 4, 1],  # Back-right face
            [3, 4, 2]   # Back-left face
        ]

        return vertices, triangles
    

    def tetrahedron(self):
        half_size = self.size / 2
        x, y, z = self.center
        height = self.size * 0.86 # Multiply by 0.86 to adjust height to make it equilateral

        vertices = [
            [x, y - height/3, z],  # Top
            [x - half_size, y + height/3, z - half_size],  # Bottom-front-left
            [x + half_size, y + height/3, z - half_size],  # Bottom-front-right
            [x, y + height/3, z + half_size]  # Bottom-back
        ]

        triangles = [
            [0, 1, 2],  # Front face
            [0, 2, 3],  # Right face
            [0, 3, 1],  # Left face
            [1, 3, 2]   # Bottom face
        ]

        return vertices, triangles
