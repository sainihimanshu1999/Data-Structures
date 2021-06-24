'''
Cloning the graph using dictionary
'''

def cloneGraph(node):
    def dfs(node):
        dic[node] = Node(node.val)
        
        for ni in node.neighbors:
            if ni not in dic:
                dfs(ni)
            dic[node].neighbors += [dic[ni]]
    dic = {}
    dfs(node)
    return dic[node]