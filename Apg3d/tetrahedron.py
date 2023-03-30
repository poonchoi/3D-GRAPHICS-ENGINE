from Apg3d.shape import Shape
from Apg3d.triangle import Triangle


class Tetrahedron(Shape):
    def __init__(self, app, size=1, center=[0, 0, 0]):
        super().__init__(app, size, center)

        self._generate_shape()

    def _generate_shape(self):
        """
        Creates points and vertices of tetrahedron

        Returns:
            [tuple[list, list]]: [tuple containing list of vertices and list of triangles]
        """
        half_size = self._size / 2
        x, y, z = self._center
        height = (
            self._size * 0.86
        )  # Multiply by 0.86 to adjust height to make it equilateral

        vertices = [
            [x, y + height / 3, z],  # Top
            [x - half_size, y - height / 3, z - half_size],  # Bottom-front-left
            [x + half_size, y - height / 3, z - half_size],  # Bottom-front-right
            [x, y - height / 3, z + half_size],  # Bottom-back
        ]

        triangles = [
            [0, 1, 2],  # Front face
            [0, 2, 3],  # Right face
            [0, 3, 1],  # Left face
            [1, 3, 2],  # Bottom face
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
