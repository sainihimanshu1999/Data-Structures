'''
In this question we basically have a range and we have to check if we can win or not, different from stone game
'''

def canIwin(maxint,total):

    visited = {}

    def canwin(choices,remainder):

        if choices[-1]>=remainder:
            return True

        key = tuple(choices)
        if key in visited:
            return visited[key]

        for i in range(len(choices)):
            if not canwin(choices[:i]+choices[i+1:],remainder-choices[i]):
                visited[key] = True
                return True

        visited[key]=False
        return False

    summi = (maxint)*(maxint+1)//2

    if summi<total:
        return False
    
    if summi==total:
        return maxint%2

    choices = list(range(1,maxint+1))
    #print(choices)

    return canwin(choices,total)

print(canIwin(10,11))