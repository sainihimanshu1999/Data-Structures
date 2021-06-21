'''
this question was sort of tricky to understand
'''

def maxSumafterPationing(arr,k):
    dp = [0]*len(arr)

    dp[0] = arr [0]
    max_so_far = arr[0]

    for i in range(k):
        max_so_far = max(max_so_far,arr[i])
        dp[i] = (i+1)*max_so_far


    for i in range(k,len(arr)):
        partition_max = 0
        for back in range(k):
            partition_max = max(partition_max,arr[i-back])
            prev_sum = dp[i-back-1]

            dp[i] = max(dp[i],prev_sum+(back+1)*partition_max)
    return dp[-1]


arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumafterPationing(arr,k))
