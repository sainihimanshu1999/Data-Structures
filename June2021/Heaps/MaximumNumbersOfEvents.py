'''we have to find the maximum number of events we can attend in a day, by using greedy and heap algorithm'''

from heapq import *


def maxEvents(events):
    events = sorted(events, key=lambda x:x[0])
    heap = []
    i,n = 0,len(events)
    count,day=0,0

    while i<n or heap:
        if not heap:
            day = events[i][0]

        while i<n and day>=events[i][0]:
            heappush(heap,events[i][1])
            i+=1

        heappop(heap)
        count +=1
        day +=1

        while heap and heap[0]<day:
            heappop(heap)

    return count

events = [[1,2],[2,3],[3,4]]
print(maxEvents(events))
 