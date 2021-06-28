'''deleting leaves in the tree'''

def removeEdge(root,target):
    if root:
        root.left = removeEdge(root.left,target)
        root.right = removeEdge(root.right,target)
        if root.val == target and not root.left and not root.right:
            root = None
    return root