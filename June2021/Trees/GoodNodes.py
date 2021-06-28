'''Good Nodes in binary tree'''


def goodNode(root):
    def count_nodes(node,value):
        if not node: return 0

        max_val = max(node.val,value)

        return (node.val>=value) + count_nodes(node.left,max_val) + count_nodes(node.right,max_val)

    return count_nodes(root,root.val)