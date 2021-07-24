'''This question have various conditions but it's not that hard once you get the logic'''


from typing import Counter


def gameLife(board):

    m = len(board)
    n = len(board[0])

    alive = set()
    neibs = []
    count = Counter()

    for i in range(m):
        for j in range(n):
            if board[i][j] ==1:
                alive.add((i,j))


    for i in range(-1,2):
        for j in range(-1,2):
            neibs.add((i,j))


    for x,y in alive:
        for i,j in neibs:
            count[(i+x,j+y)] += 1


    for i,j in count:
        if 0<=i<m and 0<=j<n:
            if count[i,j] == 3 and board[i][j]==0:
                board[i][j]=1

            if count[i,j] not in [3,4]:
                board[i][j] =0

    return board