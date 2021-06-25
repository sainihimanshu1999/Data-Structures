'''
using max heap
'''
from heapq import *

def kclosestOrigin(points,k):
    heap = []

    for x,y in points:
        dist = -(x*x+y*y)

        if len(heap) == k:
            heappushpop(heap,(dist,x,y))
        else:
            heappush(heap,(dist,x,y))


    return [[x,y] for dist,x,y in heap]
