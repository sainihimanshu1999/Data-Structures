'''
Maximum binary tree formation, we are just using basic recurrsion for this
'''

def maxBinaryTree(nums):

    if not nums:
        return None

    if len(nums)==1:
        return TreeNode(nums[0])

    maxi = max(nums)
    index = nums.index(maxi)
    root = TreeNode(nums[maxi])
    root.left = maxBinaryTree(nums[:index])
    root.right = maxBinaryTree(nums[index+1:])
    return root