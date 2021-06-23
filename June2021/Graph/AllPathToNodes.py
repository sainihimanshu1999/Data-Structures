'''
Path from source to end in graph
'''

def allPaths(graph):
    result = []
    n = len(graph)

    def dfs(node,path):
        if node == n-1:
            path.append(node)
            result.append(path)
            return result

        for ni in graph[node]:
            dfs(ni,path+[node])
    dfs(0,[])
    return result


graph =[[4,3,1],[3,2,4],[3],[4],[]]

print(allPaths(graph))