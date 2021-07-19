'''longest continous subarray with absolute difference with limit, the absolute difeerenc of each element should be less than
or equal to limit this and we do this by using heaps'''

from heapq import *

def longestSubarray(nums,limit):
    minheap = []
    maxheap = []

    result,i=0,0

    for j,num in enumerate(nums):
        heappush(maxheap, [-num,j])
        heappush(minheap,[num,j])

        while -maxheap[0][0]-minheap[0][0] > limit:
            i = min(maxheap[0][1],minheap[0][1])+1

            while maxheap[0][1]<i:
                heappop(maxheap)

            while minheap[0][1]<i:
                heappop(minheap)

        result = max(result,j-i+1)

    return result