from MatrixMath import matrix as m

class Point():
    def __init__(self, coordinate):
        self.coordinate = m.Matrix([coordinate])

    def __repr__(self):
        return str(self.coordinate[0])

a = Point([1,4,2])
print(a)