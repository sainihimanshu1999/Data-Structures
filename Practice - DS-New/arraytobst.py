def sortedArrayToBST(self, nums):
		#Code here
		if not nums:
		    return None
	    
	    mid = len(nums)//2
	    
	    root = Node(nums[mid])
        
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+1:])
        
        return root