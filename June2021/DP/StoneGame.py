'''
This question was little tricky and in dp we maintain the difference in scores of two players
'''

def stones(scores):
    n = len(scores)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = scores[i]

    for i in range(1,n):
        for j in range(n-i):
            dp[j][j+i] = max(scores[j]-dp[j+1][j+i], scores[j+i]-dp[j][j+i-1])

    return dp[0][-1]>0

scores = [1,3,1,3,4]
print(stones(scores))