'''
we have to find those vertices in graph from which we can travetse the whole graph, we come up with an very
cute solution to this answer
'''

def solve(n,edges):
    result = set(range(n))

    for i,j in edges:
        if j in result:
            result.remove(j)

    return list(result)