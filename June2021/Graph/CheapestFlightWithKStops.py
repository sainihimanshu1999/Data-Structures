'''
minimum cost of flights with k stops
'''
from collections import defaultdict

def cheapestFlight(n,flights,k,src,dst):
    graph = defaultdict(list)
    seen = defaultdict(lambda:float('inf'))

    for u,v,p in flights:
        graph[u].append((v,p))
    
    q = [(src,-1,0)]

    while q:
        pos,x,cost = q.pop(0)

        if pos==dst or  x==k:
            continue
        
        for ni,p in graph[pos]:
            if cost+p>seen[ni]:
                continue
            else:
                seen[ni] = cost+p
                q.append((ni,x+1,cost+p))

    return seen[dst] if seen[dst]<float('inf') else -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

print(cheapestFlight(n,flights,k,src,dst))