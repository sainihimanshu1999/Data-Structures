'''
In this question we use heaps and greedy algorithm
'''
from collections import defaultdict,deque
from heapq import *

def avoidFlood(rains):
    nearest = []

    location = defaultdict(deque)

    result = [-1]*(len(rains))

    for i,lake in enumerate(rains):
        location[lake].append(i)

    for i,lake in enumerate(rains):
        if nearest and nearest[0]==i:
            return []

        if lake:
            location[lake].popleft()

            if location[lake]:
                nxt = location[lake][0]
                heappush(nearest,nxt)

        else:
            if not nearest:
                result[i]= 1

            else:
                nxt_wet_day = heappop(nearest)
                wet_lake = rains[nxt_wet_day]
                result[i] = wet_lake

    return result


rains = [1,2,0,1,2]
print(avoidFlood(rains))
