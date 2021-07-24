'''This is done by simple dfs and need to be remembered for future use'''

def combinationSum(k,n):
    nums = [1,2,3,4,5,6,7,8,9]
    result = []

    def dfs(nums,target,start,path):
        if target<0:
            return 


        if target == 0:
            if len(path)==k:
                result.append(path)

        
        for i in range(start,len(nums)):
            if nums[i]>target:
                break

            dfs(nums,target-nums[i],i+1,path+[nums[i]])


    dfs(nums,n,0,[])

    return result