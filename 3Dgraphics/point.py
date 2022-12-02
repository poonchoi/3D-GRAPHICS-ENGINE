from MatrixMath.matrix import Matrix
from world import World

class Point():
    def __init__(self, world, coordinate):
        self.coordinate = Matrix([coordinate])
        world.add_point()

    def __repr__(self):
        return str(self.coordinate[0])

points = [[[32],[3]], [[3],[2]], [[32],[12]]]
projected_points = [[n, n] for n in range(len(points))]
print(points)
print(projected_points)
for shape in points:
    for point in shape:
        print(point)
        projected_points[shape][point] = [1,2,3]