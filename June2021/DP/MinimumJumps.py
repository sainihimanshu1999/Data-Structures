'''
Minimum jumps, a jump forward, b jump backward, can't jump backward twice, and we cannot jump to any forbidden  position
'''

def minJumps(forbidden,a,b,x):
    if not x: return 0 

    threshold = max(forbidden+[x])+a+b
    forbidden = set(forbidden)
    visited = set([0])
    q = [[0,0]]

    while q:
        pos,steps = q.pop(0)

        if pos+a not in forbidden and pos+a not in visited and pos+a<=threshold:
            if pos+a == x:
                return steps+1
            q.append([pos+a,steps+1])
            visited.add(pos+a)


        if pos-b>0 and pos-b not in forbidden and pos-b not in visited:
            if pos-b == x:
                return steps+1
            visited.add(pos-b)

            if pos-b+a not in forbidden and pos-b+a not in visited and pos-b+a<=threshold:
                if pos-b+a == x:
                    return steps+2
                q.append([pos-b+a,steps+2])
                visited.add(pos-b+a)

    return -1



forbidden = [14,4,18,1,15]
a = 3
b = 15
x = 9

print(minJumps(forbidden,a,b,x))