'''the steps to rotate the matrix 90 degrees 1. to interchange rows first becomes last and more 2. Transpose the matrix'''


def rotateMatrix(matrix):
    n = len(matrix)
    left = 0
    right = n-1

    while left<right:
        matrix[left],matrix[right] = matrix[right],matrix[left]
        left += 1
        right -=1


    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


    return matrix