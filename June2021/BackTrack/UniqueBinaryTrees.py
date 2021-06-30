'''This is little easy backtracking, we use dfs to make binary tree'''


def uniqueBinaryTree(n):

    if not n:
        return []

    def dfs(start,end):
        if start == end:
            return None

        result = []

        for i in range(start,end):
            for l in dfs(i,start) or [None]:
                for r in dfs(i+1,start) or [None]:
                    node = TreeNode(i)
                    node.left,node.right = l,r
                    result.append(node)


        return result

    return dfs(1,n+1)