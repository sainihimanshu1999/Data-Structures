'''finding subsets using basic dfs'''


def subsets(nums):
    result = []

    def dfs(nums,path,result):
        result.append(path)

        for i in range(len(nums)):
            dfs(nums[i+1:],path+[nums[i]],result)

    dfs(nums,[],result)
    return result

print(subsets([1,2,3]))