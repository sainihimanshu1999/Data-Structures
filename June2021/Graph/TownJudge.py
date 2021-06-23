'''
This question easy, we basically have to subtract indegree and add outdegree to the id array index we have created
'''

def townJudge(n,trust):
    result = [0]*(n+1)

    for i,j in trust:
        result[i] -= 1
        result[j] += 1

    for i in range(n+1):
        if result[i]==n-1:
            return i
    return -1


n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(townJudge(n,trust))