'''
We use sort of topological sort, we just create an adjancy set and then remove links on by one , if len of one set
is equal to one then only we can say it has shortest distance to some node
'''

def minHeight(n,edges):
    tree = [set() for i in range(n)]

    for u,v in edges:
        tree[u].add(v)
        tree[v].add(u)

    q = [x for x in range(n) if len(tree[x])<2]

    result = []

    while True:
        for x in q:
            for y in tree[x]:
                tree[y].remove(x)
                if len(tree[y])==1:result.append(y)

        if not result:
            break
        result,q = [],result
    return q

