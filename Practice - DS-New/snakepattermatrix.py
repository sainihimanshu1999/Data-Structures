def snakePattern(matrix):
    A = []
    for i in range(len(matrix)):
        if(i%2==0):
            for j in range(len(matrix)):
                A.append(matrix[i][j])
        else:
            for j in range(len(matrix)-1,-1,-1):
                A.append(matrix[i][j])
    return A