'''permutation using basic backtrack'''


def permutation(nums):
    def dfs(nums,result,path):
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:],result,path+[nums[i]])

    result  = []
    dfs(nums,result,[])
    return result



nums= [1,2,3]
print(permutation(nums))

        


