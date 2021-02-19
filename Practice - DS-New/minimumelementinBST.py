'''
class Node:
    data=0
    left=None
    right=None

'''

def minValue(root):
    if root is None:
        return -1
    curr = root
    while(curr.left is not None):
        curr = curr.left
    return curr.data