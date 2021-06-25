'''
this can be done by just using sorted but we are doing it by using heap
'''

from heapq import *


def kthLargest(nums,k):
    heap = []

    for num in nums:
        heappush(heap,num)

    for i in range(len(nums)-k):
        heappop(heap)

    return heappop(heap)


nums = [3,2,1,5,6,4]
k = 2

print(kthLargest(nums,k))
    