'''
we use recurrsion in this formula, and xor is bitwise or when both are 1 it gives and when ther is alternative it 
gives one
'''


def xorsubset(nums):
    def dfs(terms,index):
        if index == len(nums):
            return terms
        return dfs(terms,index+1)+dfs(terms^nums[index],index+1)

    return dfs(0,0)



nums = [5,1,6]
print(xorsubset(nums))