from MatrixMath.matrix import Matrix

class Point():
    def __init__(self, coordinate):
        self.coordinate = Matrix([coordinate])


    def __repr__(self):
        return str(self.coordinate[0])
        

a = Point([1,4,2])
print(a)