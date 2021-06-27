'''we have to find all possible full binary tree, a full binary tree is that tree which have either 0 or 2 children'''

def FullBinaryTree(n):
    n-=1
    if n == 1:
        return [TreeNode(0)]

    result = []

    for i in range(1,min(20,n),2):
        for left in FullBinaryTree(i):
            for right in FullBinaryTree(n-i):
                root = TreeNode(0)
                root.left = left
                root.right = right
                result += [root]


    return root