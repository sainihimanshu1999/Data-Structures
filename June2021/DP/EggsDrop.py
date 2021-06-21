'''
we have 2 eggs and m floor, if one eggs break we know we have f-1 floors to check and if both the eggs survive we have
m-f floors to check
'''


def eggDrop(n):
    def dfs(m,eggs,memo):
        if (m,eggs) in memo:
            return memo[(m,eggs)]

        if eggs==1 or m<=1:
            return m
        res = float('inf')

        for f in range(1,m+1):
            res = min(res,1+max(dfs(f-1,eggs-1,memo),dfs(m-f,eggs,memo)))
        memo[(m,eggs)] = res

        return memo[(m,eggs)]

    return dfs(n,2,{})


print(eggDrop(100))

