class Solution:
    def sortedMatrix(self,N,Mat):
        temp = [0]*(N*N)
        k = 0
        
        for i in range(N):
            for j in range(N):
                temp[k] = Mat[i][j]
                k += 1
        temp.sort()
        
        k=0
        
        for i in range(N):
            for j in range(N):
                Mat[i][j] = temp[k]
                k+=1
        return Mat