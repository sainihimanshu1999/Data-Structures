
'''This misnesweeper question is easily done using dfs algorithm, if we find in any of the adjance sqaure we will return replace
that box with count or lese e will dfs furtheer until the end of time'''


def minesweepwer(click,board):
    i,j = click
    m = len(board)
    n = len(board[0])

    def dfs(i,j):
        if board[i][j] == 'E':
            neis = [(x,y) for x,y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)) if 0<=x<m and 0<=y<n]
            
            count = sum(board[x][y] == 'M' for (x,y) in neis)

            if not count:
                board[i][j] = 'B'
                for x,y in neis:
                    dfs(x,y)

            else:
                board[i][j] = str(count)

    if board[i][j] == 'M':
        board[i][j] = 'X'

    else:
        dfs(i,j)
    return board


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]

print(minesweepwer(click,board))