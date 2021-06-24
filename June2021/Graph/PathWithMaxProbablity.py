'''
path with maximum probablity will be counted by using maxheap
'''

from collections import defaultdict
from heapq import *

def maxProb(edges,probablity,start,end):
    graph,prob = defaultdict(list),defaultdict(list)

    for i,(u,v) in enumerate(edges):
        graph[u].append(v)
        graph[v].append(u)

        prob[u,v]=prob[v,u]=probablity[i]


    visited = set()
    heap = [(-1,start)]

    while heap:
        pr,node = heappop(heap)
        if node == end:
            return -pr

        for ni in graph[node]:
            if ni in visited:
                continue
            heappush(heap,(pr*prob[node,ni],ni))
    
    return 0


n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

print(maxProb(edges,succProb,start,end))