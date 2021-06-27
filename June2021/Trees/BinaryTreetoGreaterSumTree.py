'''In greater sum tree is tree where node values is the sum of all the values present in the bst'''

from _typeshed import SupportsDivMod


def Gst(root):
    def dfs(node):
        nonlocal sumi
        if not node: return 0
        dfs(node.right)
        sumi +=node.val
        node.val = sumi
        dfs(node.left)

    sumi = 0
    dfs(root)
    return root