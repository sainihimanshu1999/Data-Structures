'''If you don't know where to start you can easily run bactracking in every direction and can start at anypoint'''


def wordSearch(board,word):
    m = len(board)
    n = len(board[0])

    def dfs(row,col,word):
        if not len(word):
            return True
        
        if row<0 or row>=m or col<0 or col>=n or board[row][col]!=word[0]:
            return False
        temp = board[row][col]
        board[row][col] = '0'
        result = dfs(row+1,col,word[1:]) or dfs(row,col+1,word[1:]) or dfs(row-1,col,word[1:]) or dfs(row,col-1,word[1:])
        board[row][col] = temp
        return result
        

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(i,j,word):
                    return True
    
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(wordSearch(board,word))