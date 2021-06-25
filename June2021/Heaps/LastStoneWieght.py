'''
Just follow these basic steps 1. put all the elements in the heap 2. pop out the two largest element 3. push the diff-
-rence in the heap back
'''

from heapq import *

def lastStone(stones):

    heap = []
    for stone in stones:
        heappush(heap,(-stone))

    while len(heap)>1:
        s1 = heappop(heap)
        s2 = heappop(heap)

        if s1!=s2:
            heappush(heap,(s1-s2))

    if len(heap)==0:
        return 0

    return -heap[0]