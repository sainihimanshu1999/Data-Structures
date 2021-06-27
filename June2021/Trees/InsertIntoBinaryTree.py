'''Basic Insertion into binary tree'''


def insertion(root,val):
    if not root:
        return TreeNode(val)

    if root.val>val:
        if root.left:
            insertion(root.left,val)
        else:
            root.left = TreeNode(val)
            return root
    elif root.val<val:
        if root.right:
            insertion(root.right,val)
        else:
            root.right = TreeNode(val)
            return root

    return root