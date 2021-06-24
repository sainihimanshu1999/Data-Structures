'''
using basic stack and and graph
'''

from collections import defaultdict

def iternary(tickets):
    graph = defaultdict(list)

    for u,v in tickets:
        graph[u].append(v)

    for u in graph.keys():
        graph[u].sort(reverse= True)

    stack = ['JFK']
    result = []

    while stack:
        i = stack[-1]

        if i in graph and len(graph[i])>0:
            stack.append(graph[i].pop())
        else:
            result.append(stack.pop())

    return result[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

print(iternary(tickets))