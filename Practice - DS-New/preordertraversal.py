def pre(root,arr):
    if root is None:
        return
    arr.append(root.data)
    pre(root.left,arr)
    pre(root.right,arr)
    

def preorder(root):
    
    res = []
    pre(root,res)
    return res