'''Basic dfs backtracking'''


def paths(graph):
    result = []
    def dfs(node,path):
        if node == n-1:
            path.append(node)
            result.append(node)
            return result
        
        for child in graph[node]:
            dfs(child,path+[node])

    dfs(0,[])
    return result