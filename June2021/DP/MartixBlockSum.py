'''
In this question we will use prefix matrix by adding both rows and columns and then finding the answer
'''

def matrixBlockSum(matrix,k):

    m = len(matrix)
    n = len(matrix[0])

    prefix = [[0]*n for _ in range(m)]

    #row prefix
    for i in range(m):
        prefix[i][0] = matrix[i][0]
        for j in range(1,n):
            prefix[i][j] = prefix[i][j-1]+matrix[i][j]

    #col prefix

    for j in range(n):
        prefix[0][j] = prefix[0][j]
        for i in range(1,m):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j]

    for i in range(m):
        ru = max(i-k,0)
        rd = min(i+k,m-1)

        for j in range(n):
            cl = max(j-k,0)
            cr = min(j+k,n-1)

            value = prefix[rd][cr]

            if ru-1>=0:
                value -= prefix[ru-1][cr]

            if cl-1>=0:
                value -= prefix[rd][cl-1]

            if ru-1>=0 and cl-1>=0:
                value += prefix[ru-1][cl-1]

            matrix[i][j]=value
    return matrix








mat = [[1,2,3],[4,5,6],[7,8,9]]
k=1
print(matrixBlockSum(mat,k))

    