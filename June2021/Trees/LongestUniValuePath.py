'''
basic dfs question,just a little bit of creative thinking needed
'''

def longestUniVal(root):
    count = 0
    def path(node):
        nonlocal count
        if not node:
            return 0
        
        left = path(node.left)
        right = path(node.right)

        left = left+1 if node.left and node.left.val == node.val else 0
        right = right+1 if node.right and node.right.val == node.val else 0

        count = max(count,left+right)
        return max(left,right)
    path(root)
    return count