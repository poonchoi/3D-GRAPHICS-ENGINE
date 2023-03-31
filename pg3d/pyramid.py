from pg3d.shape import Shape
from pg3d.triangle import Triangle


class Pyramid(Shape):
    def __init__(self, app, size=1, center=[0, 0, 0]):
        super().__init__(app, size, center)

        self._generate_shape()

    def _generate_shape(self):
        """
        Creates points and vertices of pyramid

        Returns:
            [tuple[list, list]]: [tuple containing list of vertices and list of triangles]
        """
        x, y, z = self._center
        half_size = self._size / 2

        vertices = [
            [x - half_size, y - half_size, z - half_size],  # Bottom-back-left
            [x - half_size, y - half_size, z + half_size],  # Bottom-front-left
            [x + half_size, y - half_size, z - half_size],  # Bottom-back-right
            [x + half_size, y - half_size, z + half_size],  # Bottom-front-right
            [x, y + self._size, z],  # Top
        ]

        triangles = [
            [0, 1, 2],
            [0, 2, 3],
            [1, 2, 3],  # Base face
            [0, 4, 3],  # Front-left face
            [1, 4, 0],  # Front-right face
            [2, 4, 1],  # Back-right face
            [3, 4, 2],  # Back-left face
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
