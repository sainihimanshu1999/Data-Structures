'''
this was a little tircky but it can be done by basic counter and dfs approach
'''
from collections import defaultdict,Counter
import collections

def sameLabel(n,edges,labels):
    tree =  defaultdict(list)

    for u,v in edges:
        tree[u].append(v)
        tree[v].append(u)

    result = [0]*n
    dfs(tree,labels,result,0,None)
    return result

def dfs(tree,labels,result,node,parent):
    counter = Counter()

    for child in tree[node]:
        if child == parent:
            continue
        
        counter += dfs(tree,labels,result,child,node)
    counter[labels[node]] +=1
    result[node] = counter[labels[node]]
    return counter

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"

print(sameLabel(n,edges,labels))


