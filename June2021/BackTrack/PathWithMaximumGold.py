'''Path with maximum gold, basic bactrack like island question'''


def pathofgold(grid):
    m = len(grid)
    n = len(grid)

    result = 0

    def dfs(i,j,gold):
        nonlocal result
        if 0<=i<m and 0<=j<n and grid[i][j]:
            temp = grid[i][j]
            grid[i][j] = 0

            dfs(i+1,j,gold+temp)
            dfs(i,j+1,gold+temp)
            dfs(i-1,j,gold+temp)
            dfs(i,j-1,gold+temp)

            result = max(result,gold+temp)
            grid[i][j]=temp
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                dfs(i,j,0)

    return result


grid = [[0,6,0],[5,8,7],[0,9,0]]
print(pathofgold(grid))

            