'''
we have to find minimum cost tree where we have to return the sum of non leaf nodes, where there is an inorder
traversal and through that inorder traversal the non leaf values are product of max from a slicing
'''

def mctTree(arr):
    memo = {}

    def dfs(i,j):
        if i+1==j: return 0
        if (i,j) in memo:
            return memo[(i,j)]

        for k in range(i+1,j):
            left = dfs(i,k)
            right = dfs(k,j)
            root = max(arr[i:k])*max(arr[k:j])
            total = root+left+right
            ans = min(ans,total)
        memo[(i,j)] = ans
        return memo[(i,j)]

    return dfs(0,len(arr))
