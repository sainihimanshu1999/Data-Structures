'''Longest increasing susequence using dp basically'''

def longestIncreasing(nums):
    if not nums:
        return 0

    length = [1]*nums

    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                if length[i] == length[j]:
                    length[i] = length[j]+1

    return max(length)