'''
we use heaps to store our result, because it onlhy has O(logk) time of push and pop and we can save memory by using
just the required size of answer and we are going to use binary search to find the count of the soldiers
'''
from heapq import *

def weakestRow(matrix,k):
    heap = []

    for i,row in enumerate(matrix):
        soldierCount = binary(row)

        if len(heap) == k:
            heappushpop(heap,(-soldierCount,-i))
        else:
            heappush(heap,(-soldierCount,-i))

    result = []
    while heap:
        result.append(-heappop(heap)[1])

    return result[::-1]

def binary(row):
    low,high = 0,len(row)-1

    while low<high:
        mid = (low+high+1)//2

        if not row[mid]:
            high = mid-1
        else:
            low = mid

    if row[0]:
        low+=1
    return low


mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(weakestRow(mat,k))