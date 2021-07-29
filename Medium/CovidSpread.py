from collections import deque

def covid(mat):
    m, n = len(mat), len(mat[0])
    q = deque([(i, j) for i in range(m) for j in range(n) if mat[i][j]])
    #print(q)
    while q:
        print(q)
        i, j = q.popleft()
        for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            print(x,y)
            if 0 <= x < m and 0 <= y < n and not mat[x][y]:
                mat[x][y] = mat[i][j] + 1
                print(matrix)
                q.append((x, y))
    return mat[i][j]



matrix = [[0,0,0,0],[0,0,0,1],[0,1,0,0]]

print(covid(matrix))