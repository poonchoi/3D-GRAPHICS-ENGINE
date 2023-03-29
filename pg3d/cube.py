from pg3d.shape import Shape
from pg3d.triangle import Triangle


class Cube(Shape):
    def __init__(self, app, size=1, center=[0, 0, 0]):
        super().__init__(app, size, center)

        self._generate_shape()

    def _generate_shape(self):
        """
        Creates points and vertices of cube

        Returns:
            [tuple[list, list]]: [tuple containing list of vertices and list of triangles]
        """
        x, y, z = self._center
        half_size = self._size / 2

        vertices = [
            [x - half_size, y + half_size, z + half_size],  # Front-bottom-left
            [x + half_size, y + half_size, z + half_size],  # Front-bottom-right
            [x + half_size, y - half_size, z + half_size],  # Front-top-right
            [x - half_size, y - half_size, z + half_size],  # Front-top-left
            [x - half_size, y + half_size, z - half_size],  # Back-bottom-left
            [x + half_size, y + half_size, z - half_size],  # Back-bottom-right
            [x + half_size, y - half_size, z - half_size],  # Back-top-right
            [x - half_size, y - half_size, z - half_size],  # Back-top-left
        ]

        triangles = [
            [0, 1, 2],
            [0, 2, 3],  # Front face
            [1, 5, 6],
            [1, 6, 2],  # Right face
            [3, 2, 6],
            [3, 6, 7],  # Top face
            [4, 5, 1],
            [4, 1, 0],  # Bottom face
            [4, 0, 3],
            [4, 3, 7],  # Left face
            [7, 6, 5],
            [7, 5, 4],  # Back face
        ]

        if (triangles != None) and (vertices != None):
            for triangle in triangles:
                Triangle(
                    self.app,
                    [
                        vertices[triangle[0]],
                        vertices[triangle[1]],
                        vertices[triangle[2]],
                    ],
                )
