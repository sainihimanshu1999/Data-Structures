def countNonLeafNodes(root):
    if root is None:
        return 0
    elif(root.left is None and root.right is None):
        return 0
    else:
        return (1+countNonLeafNodes(root.left)+countNonLeafNodes(root.right))