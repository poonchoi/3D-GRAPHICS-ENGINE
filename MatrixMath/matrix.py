def zeroes(height, width): # need to finish
    """
    Creates a matrix of size h x w and fills it with zeroes
    """
    matrix = [[0 for w in range(width)] for h in range(height)]
    return Matrix(matrix)


class Matrix():
    def __init__(self, matrix):
        """
        Gets the height and width of the matrix
        """
        self.matrix = matrix
        self.width = len(self.matrix[0])
        self.height = len(self.matrix)


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


    def __getitem__(self, index):
        """
        Defines behavior of using square brackets on Matrix objects

        E.g:
        > a = Matrix([1,2,3],[4,5,6])
        > a[0]
          [1,2,3]
        """
        return self.matrix[index] 
    

    def __rmul__(self, value):
        """
        Defines behaviour of multiplying matrix object with non-matrix object
        """
        if isinstance(value, int) or isinstance(value, float): # checks if the value is a number
            result = zeroes(self.height, self.width)
            for h in range(self.height):
                for w in range(self.w):
                    pass
        return None


    def __mul__(self, other):
        """
        Defines the behaviour of the * operator
        """
        a = self.matrix
        b = other
        cols_a = self.width
        rows_a = self.height
        cols_b = other.width
        rows_b = other.height

        try:
            if cols_a == rows_b:
                result = zeroes(rows_a, cols_b)
                for i in range(rows_a):
                    for j in range(cols_b):
                        sum = 0
                        for k in range(cols_a):
                            sum += a[i][k] * b[k][j]
                        result[i][j] = sum
                return result
            elif cols_b == rows_a:
                result = zeroes(rows_b, cols_a)
                for i in range(rows_b):
                    for j in range(cols_a):
                        sum = 0
                        for k in range(cols_b):
                            sum += b[i][k] * a[k][j]
                        result[i][j] = sum
                return result
            else:
                return ("ROWS OF ONE MATRIX MUST EQUAL COLUMNS OF THE OTHER")
        except:
            return ("ERROR OCCURED")