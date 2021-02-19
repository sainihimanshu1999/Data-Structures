def postorder(root,arr):
    if root is None:
        return 
    postorder(root.left,arr)
    postorder(root.right,arr)
    arr.append(root.data)


def postOrder(root):
    '''
    :param root: root of the given tree.
    :return the list containing post order traversal of the given binary tree.
    '''
    # code here
    res = []
    postorder(root,res)
    return res