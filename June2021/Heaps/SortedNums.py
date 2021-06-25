'''
we use counting sort in this question
'''
from collections import Counter

def sortedNums(nums):
    count = Counter(nums)
    min_num = min(nums)
    max_num = max(nums)

    result = []
    for i in range(min_num,max_num+1):
        result.extend([i]*count[i])

    return result

nums = [5,2,3,1]
print(sortedNums(nums))
