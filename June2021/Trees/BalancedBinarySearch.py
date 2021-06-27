''' converting into inorder and then converting into binary balanced'''

def balancedBinary(root):
    def ino(root):
        ino(root.left)
        arr.append(root.val)
        ino(root.right)

    arr = []

    ino(root)

    def construct(arr):
        if not arr:
            return None

        mid = len(arr)//2
        node = TreeNode(arr[mid])
        node.left = construct(arr[:mid])
        node.right = construct(arr[mid+1:])
        return node
    return construct(root)
