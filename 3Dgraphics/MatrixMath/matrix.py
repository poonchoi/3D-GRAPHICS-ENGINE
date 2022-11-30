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
        # loop that iterates throguh every item of the matrix
        for height in range(self.height):
            print("[",end="")
            for width in range(self.width):
                if width != self.width-1: # if the number isnt the last in its row
                    print(f"{self.matrix[height][width]}, ",end="")
                else:
                    print(f"{self.matrix[height][width]}",end="") # if the number is that last in its row
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
                for w in range(self.width):
                    result[h][w] == self.matrix[h][w] * value
            return result
        else:
            return "ERROR OCCURED"


    def __mul__(self, other):
        """
        Defines the behaviour of the * operator
        """
        try:
            if self.width == other.height:
                result = zeroes(self.height, other.width)
                for h in range(self.height):
                    for w in range(other.width):
                        sum = 0
                        for k in range(self.width):
                            sum += self.matrix[h][k] * other[k][w]
                        result[h][w] = sum
                return result
            elif other.width == self.height:
                result = zeroes(other.height, self.width)
                for h in range(other.height):
                    for w in range(self.width):
                        sum = 0
                        for k in range(other.width):
                            sum += other[h][k] * self.matrix[k][w]
                        result[h][w] = sum
                return result
            else:
                return ("ROWS OF ONE MATRIX MUST EQUAL COLUMNS OF THE OTHER")
        except:
            return ("ERROR OCCURED")