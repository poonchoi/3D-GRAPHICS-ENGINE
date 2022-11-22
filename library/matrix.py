class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.cols = len(matrix)
        self.rows = len(matrix[0])
    
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
        a = self.matrix
        b = other
        cols_a = len(a[0])
        rows_a = len(a)
        cols_b = len(b[0])
        rows_b = len(b)
        cols_a = self.cols
        rows_a = self.rows
        cols_b = other.cols
        rows_b = other.rows

        if cols_a == rows_b:
            result = [[j for j in range(cols_b)] for i in range(rows_a)]
            for i in range(rows_a):
                for j in range(cols_b):
                    sum = 0
                    for k in range(cols_a):
                        sum += a[i][k] * b[k][j]
                    result[i][j] = sum
            return result

x = [1, 3, -5]
y = [4, -2, -1]

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

print(dot(x, y))