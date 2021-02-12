def countZeros(A, N):
    temp = [0]*(N*N)
    k = 0
    for i in range(N):
        for j in range(N):
            temp[k] = A[i][j]
            k += 1
    return(temp.count(0))