from MatrixMath.matrix import Matrix

class World_Space:
    def __init__(self):
        self.all_shapes = []
        self.__PROJECT_MATRIX = Matrix([[1, 0, 0],
                                      [0, 1, 0]
                                      [0, 0, 0]])


    def add_shape(self, shape):
        pass


    def project(self, point):
        return point * self.__PROJECT_MATRIX

    
    def rotate_x(self, angle):
        pass


    def rotate_y(self, angle):
        pass


    def rotate_z(self, angle):
        pass


    def translate(self, new_pos):
        pass


    def draw(self):
        pass


    def check_movement(self):
        pass


    def run(self):
        pass