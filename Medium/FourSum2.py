'''we use dictionary in four sum'''

from collections import defaultdict

def fourSum(nums1,nums2,nums3,nums4):
    result = 0
    dic = defaultdict(int)

    for a in nums1:
        for b in nums2:
            dic[a+b] +=1


    for c in nums3:
        for d in nums4:
            result += dic[-c-d]

    return result