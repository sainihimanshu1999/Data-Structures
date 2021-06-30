'''Making square using the matchsticks present, basic intution is to check if we can divde array into 4 subarray
whose sum will be eqaul to the possible side of the sqaure'''


def matchStick(nums):
    if not nums:
        return False

    n = len(nums)
    perimeter = sum(nums)

    side = perimeter//4

    if side*4!=perimeter:
        return False

    nums.sort(reverse = True)
    result = [0 for _ in range(4)]

    def dfs(index):
        if index == n:
            return result[0]==result[1]==result[2]==side

        for i in range(4):
            if result[i]+nums[index]<=side:
                result[i]+=nums[index]
                if dfs(index+1):
                    return True
                result[i]-=nums[index]
        return False

    return dfs(0)


nums = [1,1,1,2,2]
print(matchStick(nums))