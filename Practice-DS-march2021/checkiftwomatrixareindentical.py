'''
Program to check that the two matrix that are given are identical or not
'''

'''
for two matrix to be equal, the number of rown and columns should be equal as well as there elemnts 
should be equal too
'''

def aresame(A,B):
    n = 4 #4*4 matrix
    for i in range(n):
        for j in range(n):
            if (A[i][j] != B[i][j]):
                return 0
    return 1
    
