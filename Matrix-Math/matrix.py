def zeroes(height, width): # need to finish
    """
    Creates a matrix of size h x w and fills it with zeroes
    """
    matrix = [[0 for w in range(width)] for h in range(height)]
    return Matrix(matrix)


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.width, self.height, self.is_vector = self.initialize_attributes()

    
    def initialize_attributes(self):
        try: # this is if the matrix is actually a matrix
            width = len(self.matrix[0])
            height = len(self.matrix)
            is_vector = False
        except TypeError: # this is here if the matrix is actually a vector
            width = len(self.matrix)
            height = 1
            is_vector = True

        return width, height, is_vector


    def __repr__(self):
        """
        Defines behaviour of printing a Matrix object
        """
        if self.is_vector == False:
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
        else:
            print("[",end="")
            for width in range(self.width):
                if width != self.width-1:
                    print(f"{self.matrix[width]} ",end="")
                else:
                    print(f"{self.matrix[width]}",end="")
                
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
        if isinstance(value, int) or isinstance(value, float):
            result = zeroes(self.height, self.width)
            for h in range(self.height):
                for w in range(self.w):
                    pass


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

        if a.is_vector == False and b.is_vector == False: # neither are vectors
            try:
                if cols_a == rows_b:
                    # result = Matrix([[j for j in range(cols_b)] for i in range(rows_a)]) # replace with zeroes function
                    result = zeroes(rows_a, cols_b)
                    for i in range(rows_a):
                        for j in range(cols_b):
                            sum = 0
                            for k in range(cols_a):
                                sum += a[i][k] * b[k][j]
                            result[i][j] = sum
                    return result
                elif cols_b == rows_a:
                    # result = Matrix([[j for j in range(cols_a)] for i in range(rows_b)]) # replace with zeroes function
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
        elif a.is_vector == True and b.is_vector == False: # only a is a vector
            return ("havent made this yet")
        elif a.is_vector == False and b.is_vector == True: # only b is a vector
            return ("havent made this yet")
        elif a.is_vector == True and b.is_vector == True: # both are vectors
            return ("havent made this yet")