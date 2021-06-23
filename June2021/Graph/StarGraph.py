'''
In start graph every node is connected to the star in centre to we can solve it easily
'''

def starGraph(edges):
    x,y = edges[0][0],edges[0][1]

    if x==edges[1][0] or x==edges[1][1]:
        return x
    return y