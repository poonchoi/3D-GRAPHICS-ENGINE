from pg3d.triangle import Triangle


class Shape:
    def __init__(self, app, shape, size=1, center=[0, 0, 0]):
        """
        Initialises shape

        Args:
            app ([App]): [Specify app object]
            shape ([str]): [Specify shape]
            size (float, optional): [Size of shape]. Defaults to 1.
            center (list, optional): [Center coordinate of shape]. Defaults to [0, 0, 0].
        """
        self.app = app

        self._center = center
        self._size = size

        triangles, vertices = None, None

        if shape.lower() == "cube":
            vertices, triangles = self._cube()
        elif shape.lower() == "pyramid":
            vertices, triangles = self._pyramid()
        elif shape.lower() == "tetrahedron":
            vertices, triangles = self._tetrahedron()

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

    def _cube(self):
        """
        Creates points and vertices of cube

        Returns:
            [tuple[list, list]]: [tuple containing list of vertices and list of triangles]
        """
        x, y, z = self._center
        half_size = self._size / 2

        vertices = [
            [x - half_size, y - half_size, z + half_size],  # Front-bottom-left
            [x + half_size, y - half_size, z + half_size],  # Front-bottom-right
            [x + half_size, y + half_size, z + half_size],  # Front-top-right
            [x - half_size, y + half_size, z + half_size],  # Front-top-left
            [x - half_size, y - half_size, z - half_size],  # Back-bottom-left
            [x + half_size, y - half_size, z - half_size],  # Back-bottom-right
            [x + half_size, y + half_size, z - half_size],  # Back-top-right
            [x - half_size, y + half_size, z - half_size],  # Back-top-left
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

        return vertices, triangles

    def _pyramid(self):
        """
        Creates points and vertices of pyramid

        Returns:
            [tuple[list, list]]: [tuple containing list of vertices and list of triangles]
        """
        x, y, z = self._center
        half_size = self._size / 2
        height = self._size

        vertices = [
            [x - half_size, y + half_size, z - half_size],  # Bottom-back-left
            [x - half_size, y + half_size, z + half_size],  # Bottom-front-left
            [x + half_size, y + half_size, z - half_size],  # Bottom-back-right
            [x + half_size, y + half_size, z + half_size],  # Bottom-front-right
            [x, y - half_size, z],  # Top
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

        return vertices, triangles

    def _tetrahedron(self):
        """
        Creates points and vertices of tetrahedron

        Returns:
            [tuple[list, list]]: [tuple containing list of vertices and list of triangles]
        """
        half_size = self._size / 2
        x, y, z = self._center
        height = (
            self.size * 0.86
        )  # Multiply by 0.86 to adjust height to make it equilateral

        vertices = [
            [x, y - height / 3, z],  # Top
            [x - half_size, y + height / 3, z - half_size],  # Bottom-front-left
            [x + half_size, y + height / 3, z - half_size],  # Bottom-front-right
            [x, y + height / 3, z + half_size],  # Bottom-back
        ]

        triangles = [
            [0, 1, 2],  # Front face
            [0, 2, 3],  # Right face
            [0, 3, 1],  # Left face
            [1, 3, 2],  # Bottom face
        ]

        return vertices, triangles
