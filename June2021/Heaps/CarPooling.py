'''
In this question we use heap 
'''

from heapq import *

def carPool(trips,capacity):
    trips = sorted(trips,key=lambda x:x[1])
    heap = []
    max_load,curr_load = 0,0

    for load,start,end in trips:
        while heap and start>=heap[0][0]:
            curr_load -= heap[0][1]
            heappop(heap)

        heappush(heap,(end,load))

        curr_load += load
        max_load = max(max_load,curr_load)
    return max_load<=capacity



trips = [[2,1,5],[3,5,7]]
capacity = 3
print(carPool(trips,capacity))