def getSize(node):
    # code here
    if node is None:
        return 0
    else:
        return (getSize(node.left)) + 1 + getSize(node.right)