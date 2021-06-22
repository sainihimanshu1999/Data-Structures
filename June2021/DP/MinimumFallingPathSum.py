'''
Basic intuive question rather than going up to down in dp, we tried going row by row, summing
'''

def minFallingPath(grid):
    m,n=len(grid),len(grid[0])

    for i in range(1,m):
        for j in range(n):
            if j==0:
                grid[i][j] += min(grid[i-1][j],grid[i-1][j+1])
            if 0<j<n-1:
                grid[i][j] += min(grid[i-1][j],grid[i-1][j+1],grid[i-1][j-1])
            if j == n-1:
                grid[i][j] += min(grid[i-1][j],grid[i-1][j-1])

    return min(grid[n-1])


matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(minFallingPath(matrix))