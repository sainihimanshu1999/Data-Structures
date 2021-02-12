def sumTriangles(matrix, n):
    su = 0
    sl = 0
    for i in range(n):
        for j in range(n):
            if(i<=j):
                su += matrix[i][j]
    
    for i in range(n):
        for j in range(n):
            if(j<=i):
                sl += matrix[i][j]
                
    return(su,sl)