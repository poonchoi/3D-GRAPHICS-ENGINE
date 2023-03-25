class mat(list):
    def __matmul__(self, B):
        A = self
        return mat([[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0])) ] for i in range(len(A))])

d = mat([[1,3],[7,5]])
B = mat([[6,8],[4,2]])

print(d @ B)


##########################


def matmul(a, b):
    result = [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0])) ] for i in range(len(a))]
    # for i in range(len(a)):
    #     for j in range(len(b[0])):
    #         for k in range(len(b)):
    #             result.append([sum(a[i][k] * b[k][j])])
    return result

print(matmul(d,B))