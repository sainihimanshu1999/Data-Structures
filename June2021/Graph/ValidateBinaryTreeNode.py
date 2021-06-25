'''
two rules of binary tree, 1st if there are exactly n-1 edges if there is n nodes 2st every node, except parent has parent node
'''

def validateBinaryTreeNode(n,leftChild,rigthChild):
    leftEdges = len([l for l in leftChild if l!= -1])
    rigthEdges = len([r for r in rigthChild if r != -1])

    if leftEdges+rigthEdges != n-1:
        return False


    parent = [[] for _ in range(n)]

    for i in range(n):
        if leftChild[i]!= -1:
            parent[leftChild[i]].append(i)

        if rigthChild[i]!=-1:
            parent[rigthChild[i]].append(i)

    for i in range(n):
        if parent[i] and parent[parent[i][0]] == [i]:
            return False

    roots = [i for i in range(len(parent)) if not parent[i]]
    if len(roots) !=1:
        return False

    root = roots[0]

    return max(leftChild[root],rigthChild[root]) or n==1