'''
it's pretty easy we just have to check for even grandparents
'''

def evenGrandParents(root):
    def dfs(node,parent,grandParent):
        nonlocal sumi
        if not node: return 0
        if parent and grandParent and grandParent.val%2==0:
            sumi += node.val

        dfs(node.left,node,parent)
        dfs(node.right,node,parent)

    sumi = 0
    dfs(root,None,None)
    return sumi
