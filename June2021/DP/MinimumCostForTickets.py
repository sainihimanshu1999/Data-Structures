'''
we have 1 day 7 day and 30 days pass and we calculate the minimum cost of travelling by calculating back our expenses
by going back in time
'''

def minCost(days,costs):
    dp = [-1]*366

    dp[0] = 0

    for day in days:
        dp [day] = 0

    for i in range(1,366):
        if dp[i] == -1:
            dp[i] = dp[i-1]

        else:
            dp[i] = min(dp[i-1]+costs[0], dp[max(i-7,0)]+costs[1], dp[max(i-30,0)]+costs[2])

    return dp[365]


days = [1,4,6,7,8,20]
costs = [7,2,15]

print(minCost(days,costs))