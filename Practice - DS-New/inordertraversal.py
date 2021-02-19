def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)

# Return a list containing the inorder traversal of the given tree
def InOrder(root):
    a = []
    inorder(root,a)
    return a