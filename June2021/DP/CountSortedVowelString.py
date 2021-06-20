'''
This question can be done in two ways, first one being dp and other being the basic permutation
'''

def vowles(n):
    visited = {}
    def dfs(n,k):
        if n==1 or k==1 : return k
        if (n,k) in visited:
            return visited[n,k]

        visited[n,k] = sum(dfs(n-1,i) for i in range(1,k+1))

        return visited[n,k]

    return dfs(n,5)



def vowels2(n):
    return (n+1)*(n+2)*(n+3)*(n+4)//24

print(vowels2(23333))