from pg3d.triangle import Triangle
from pg3d.point import Point

class Model:
    def __init__(self, app, path):
        self.app = app
        self.path = path
        self.draw_model()

    def draw_model(self):
        vertices, triangles = [], []
        with open(self.path) as file:
            for line in file:
                if line.startswith("v "):
                    vertices.append([float(i) for i in line.split()[1:]])
                elif line.startswith("f "):
                    faces = line.split()[1:]
                    triangles.append([int(face.split("/")[0]) - 1 for face in faces])
        
        if len(triangles) > 0:
            for triangle in triangles:
                Triangle(self.app, (vertices[triangle[0]], vertices[triangle[1]], vertices[triangle[2]]))
        else:
            for vertex in vertices:
                Point(self.app, vertex)
