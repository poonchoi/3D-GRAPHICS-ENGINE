def zeroes():
    """
    Creates a matrix of size h x w and fills it with zeroes
    """
    pass

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
    
    def __repr__(self):
        """
        Defines behaviour of printing a Matrix object
        """
        print("[",end="")
        for height in range(self.height):
            print("[",end="")
            for width in range(self.width):
                if width != self.width-1:
                    print(f"{self.matrix[height][width]} ",end="")
                else:
                    print(f"{self.matrix[height][width]}",end="")
            if height != self.height-1:
                print("]")
            else:
                print("]",end="")
        print("]",end="")
        return ("")

    def __rmul__(self, other):
        """
        Defines the behaviour when the matrix object is on the right of the * operator
        """
        pass

    def __getitem__(self, index):
        """
        Defines behavior of using square brackets on Matrix objects

        E.g:
        > a = Matrix([1,2,3],[4,5,6])
        > a[0]
          [1,2,3]
        """
        return self.matrix[index] 

    def __mul__(self, other):
        """
        Defines the behaviour of the * operator
        """
        a = self.matrix
        b = other
        # cols_a = len(a[0])
        # rows_a = len(a)
        # cols_b = len(b[0])
        # rows_b = len(b)
        cols_a = self.width
        rows_a = self.height
        cols_b = other.width
        rows_b = other.height

        if cols_a == rows_b:
            result = Matrix([[j for j in range(cols_b)] for i in range(rows_a)]) # replace with zeroes function
            for i in range(rows_a):
                for j in range(cols_b):
                    sum = 0
                    for k in range(cols_a):
                        sum += a[i][k] * b[k][j]
                    result[i][j] = sum
            return result

x = Matrix([[1,2,3]])
y = Matrix([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]])

result = x*y
print(result)

### TESTING MATRIX MULTIPLICATION FUNCTION ###

x = [[12, 0],
     [0, 13]]
y = [[4, 1],
     [1, 5]]

d = [[1, 2, 3]]
g = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]

def dot(a, b):
    cols_a = len(a[0])  
    rows_a = len(a)
    cols_b = len(b[0])
    rows_b = len(b)

    if cols_a == rows_b:
        result = [[j for j in range(cols_b)] for i in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                sum = 0
                for k in range(cols_a):
                    sum += a[i][k] * b[k][j]
                result[i][j] = sum
        return result

# print(dot(x, y))
# print(dot(d, g))

##############################################