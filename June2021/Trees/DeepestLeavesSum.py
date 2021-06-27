'''This question can be done by two methods one is bfs and other is dfs(we will use 2 dfs, dfs1 to find the max depth
and dfs2 to fins the sum of node leaves at those values'''

#BFS
def deepestLeaves(root):
    result = []
    q = [root]

    while q:
        sumi = 0
        for i in range(len(q)):
            node = q.pop(0)
            sumi += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        result.append(sumi)

    return result[-1]


#DFS

def deepestLeaves2(root):
    def dfs1(node):
        if not node: return 0
        return max(dfs1(node.left),dfs1(node.right))+1

    def dfs2(node,d):
        nonlocal ans
        if not node: return
        if d == depth:
            ans += node.val
        dfs2(node.left,d+1)
        dfs2(node.right,d+1)

    ans = 0
    depth = dfs1(root)        
    dfs2(root,1)
    return ans