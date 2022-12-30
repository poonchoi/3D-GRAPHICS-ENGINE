def zeroes(height, width):
    """
    Creates a matrix of size h x w and fills it with zeroes
    this uses nested list comprehension
    """
    return Matrix([[0 for w in range(width)] for h in range(height)])


def identity(n):
    """
    Returns an identity matrix of size n x n
    """
    matrix = zeroes(n, n)
    for i in range(matrix.height):
        matrix[i][i] = 1

    return matrix


def copy_matrix(matrix):
    return Matrix([[matrix[h][w] for w in range(len(matrix[0]))] for h in range(len(matrix))])


class Matrix():
    def __init__(self, matrix):
        """
        initialises the matrix and finds the height and width of the matrix
        """
        self.matrix = matrix
        self.width = len(self.matrix[0])
        self.height = len(self.matrix)


    def __repr__(self):
        """
        Defines behavior of printing a matrix object
        """
        print("[",end="")
        # loop that iterates through every item of the matrix
        for height in range(self.height):

            print("[",end="")
            for width in range(self.width):

                if width != self.width-1: # if the number is'nt the last in its row
                    print(f"{self.matrix[height][width]}, ",end="")

                else:
                    print(f"{self.matrix[height][width]}",end="") # if the number is that last in its row

            if height != self.height-1:
                print("]")

            else:
                print("]",end="")

        print("]",end="")

        return ("")


    def __setitem__(self, index, value):
        """
        Defines the behaviour of changing the value of the matrix at a specific value
        """
        self.matrix[index] = value


    def __getitem__(self, index):
        """
        Defines behavior of using square brackets on matrix objects

        E.g:
        > a = Matrix([1,2,3],[4,5,6])
        > a[0]
          [1,2,3]
        """
        return self.matrix[index] 


    def __rmul__(self, value):
        """
        Defines behavior of multiplying matrix object with non-matrix object
        """
        if isinstance(value, int) or isinstance(value, float): # checks if the value is a number
            result = zeroes(self.height, self.width)

            # iterates through each number and multiplies it with the value
            for height in range(self.height):

                for width in range(self.width):
                    result[height][width] =  self.matrix[height][width] * value
            
            return result

        else:
            return "ERROR OCCURRED"


    def __mul__(self, other):
        """
        Defines the behavior of the * operator for multiplication
        """
        try:
            if self.width == other.height:
                result = zeroes(self.height, other.width)

                for height in range(self.height):

                    for width in range(other.width):
                        sum = 0

                        for other_height in range(self.width):
                            sum += self.matrix[height][other_height] * other[other_height][width]

                        result[height][width] = sum

                return result

            elif other.width == self.height:
                result = zeroes(other.height, self.width)

                for height in range(other.height):

                    for width in range(self.width):
                        sum = 0

                        for other_height in range(other.width):
                            sum += other[height][other_height] * self.matrix[other_height][width]

                        result[height][width] = sum

                return result

            else:
                return ("ROWS OF ONE MATRIX MUST EQUAL COLUMNS OF THE OTHER")

        except:
            return ("ERROR OCCURRED")
    

    def identity(self, n):
        """
        Returns an identity matrix of size n x n
        """
        matrix = zeroes(n, n)
        # iterates through each value of matrix
        for i in range(len(matrix)):

            for j in range(len(matrix)):

                if i == j: # is a diagonal
                    matrix[i][j] = 1

                else: # isnt a diagonal
                    matrix[i][j] = 0

        return matrix


    def transpose(self):
        """
        Returns a transposed copy of the matrix
        """
        # 1. uses the zip function to transpose the unpacked matrix
        # 2. uses the map function to turn the sets into lists
        return Matrix(list(map(list,zip(*self.matrix))))


    def minor(self, i, j):
        """
        Returns a copy of the matrix with the row and column, i and j, deleted
        """
        if self.is_square():
            # removes the i-th row and j-th column using slicing
            return Matrix([row[:j] + row[j+1:] for row in (self.matrix[:i]+self.matrix[i+1:])])
        
        else:
            print("CANNOT FIND MINOR OF NON-SQUARE MATRIX")
    

    def determinant(self):
        """
        Returns the determinant of a function using the method of cofactors
        """
        if self.is_square():
            # returns the determinant of a 1x1 matrix
            if self.height == 1:
                return self.matrix[0][0]

            determinant = 0

            for i, value in enumerate(self.matrix[0]): # iterate over elements in first row of matrix
                minor = self.minor(0, i) # calculate minor at position [0, i]
                determinant += (-1)**i * value * minor.determinant() # cofactor formula
            
            return determinant
        else:
            print("CANNOT FIND DETERMINANT OF A NON-SQUARE MATRIX")
    
    def inverse(self):
        """
        Returns the inverse of the matrix using Gauss-Jordan Elimination method
        """
        # check if matrix isnt square
        if not self.is_square():
            print("CANNOT FIND INVERSE OF NON-SQUARE MATRIX")

        else:
            # check if matrix determinat is equal to 0
            if self.determinant == 0:
                print("CANNOT FIND INVERSE OF MATRIX WITH DETERMINANT = 0")

            # if both conditions are not met, the inverse will be calculated
            else:
                I = identity(self.height)
                # copies of matrix and identity matrix are made
                M_copy = copy_matrix(self.matrix)
                I_copy = copy_matrix(I.matrix)
                
                indicies = list(range(self.height)) # list of all the indicies in the matrix row

                for cd in range(self.height): # cd = current diagonal
                    cd_factor = 1 / M_copy[cd][cd]
                    
                    # divide all the values in the current row by the diagonal item
                    # this is done to make the diagonal item equal to one
                    for i in range(self.height):
                        M_copy[cd][i] *= cd_factor
                        I_copy[cd][i] *= cd_factor
                
                    for j in indicies[:cd] + indicies[cd+1:]:
                        cr_factor = M_copy[j][cd] # cr = current row

                        # subtract the current value by the pivot on its row multiplied by the value on the row above
                        for k in range(self.height):
                            M_copy[j][k] -= (M_copy[cd][k] * cr_factor)
                            I_copy[j][k] -= (I_copy[cd][k] * cr_factor)

                return I_copy


    def is_square(self):
        """
        Checks whether the matrix is a square matrix

        SQUARE MATRIX:  |   NON-SQUARE MATRIX:
        [[1,2],         |   [[1,2,3],
         [3,4]]         |    [4,5,6]]
        """
        if self.width == self.height:
            return True
            
        else:
            return False