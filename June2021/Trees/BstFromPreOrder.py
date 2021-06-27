'''There are two ways of forming bst with given preorder array, one using recursion and one using iterative stack'''


#recursion

def contruct(preorder):
    if not preorder: return None

    root = TreeNode(preorder[0])
    i = 1

    while i<len(preorder) and preorder[i]<preorder[0]:
        i+=1

    root.left = contruct(preorder[1:i])
    root.right = contruct(preorder[i:])

    return root


# stack iterative


def construct2(preorder):
    root = TreeNode(preorder[0])
    stack = [root]

    for value in preorder[1:]:
        if value<stack[-1].value:
            stack[-1].left = TreeNode(value)
            stack.append(stack[-1].left)

        else:
            while stack and stack[-1].val<value:
                last = stack.pop()
            last.right = TreeNode(value)
            stack.append(last.right)

    return root
