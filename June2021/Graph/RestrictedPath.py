'''
To find restrincted path in the graph, first wew have to find the shortest distance from the node and then use 
this distance to check if neighbour's distance is lesser than source itself(for this check we use dfs)
'''
from collections import defaultdict
from heapq import *

def restrictedPath(n,edges):
    if n==1: return 0

    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((w,v))
        graph[v].append((w,u))


    def dijsktra():
        heap = [(n,0)]
        dist = [float('inf')]*(n+1)

        dist[n] = 0

        while heap:
            u,d  = heappop(heap)
            if d!=dist[u]:
                continue
            for w,v in graph[u]:
                if dist[v]>dist[u]+w:
                    dist[v] = dist[u]+w
                    heappush(heap,(v,dist[v]))

        return dist

    def dfs(src):
        if src ==n:
            return 1
        ans = 0
        for w,v in graph[src]:
            if dist[src]>dist[v]:
                ans = (ans+dfs(v))
        return ans

    dist = dijsktra()
    return dfs(1)
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(restrictedPath(n,edges))
