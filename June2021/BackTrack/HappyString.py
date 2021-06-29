'''
Happy string is that string which only contains a b c and is lexographically ordered
'''

from collections import deque

def happyString(n,k):
    graph = {'a':'bc','b':'ac','c':'ab'}
    q = deque(['a','b','c'])

    while len(q[0])!=n:
        u = q.popleft()
        for v in graph[u[-1]]:
            q.append(u+v)

    return q[k-1] if len(q)>=k else ''



n = 3
k = 9

print(happyString(n,k))