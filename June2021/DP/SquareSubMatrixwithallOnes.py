'''
to check if the square matrix has all ones we just have to check it's adjacent 3 sides, if they are one we can increment
our result
'''

def allOnes(matrix):

    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    result = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                if i == 0 or j== 0:
                    result+=1
                else:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])
                    result+=matrix[i][j]

    return result


matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(allOnes(matrix))
