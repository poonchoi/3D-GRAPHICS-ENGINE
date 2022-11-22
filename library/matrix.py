class mat():
    def __init__(self, matrix):
        self.matrix = matrix

    def __mul__(self, other):
        a = self.matrix
        b = other
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
