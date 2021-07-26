'''In this question we are going to count the substrings in which 0 and 1 are equal'''

def binarySubstring(s):
    stack = [[],[]]

    curr = int(s[0])
    stack[curr].append(curr)
    result = 0


    for i in range(1,len(s)):
        v = int(s[i])

        if v != curr:
            stack[v].clear
            curr = v

        stack[v].append(v)

        if len(stack[1-v])>0:
            stack[1-v].pop()
            result +=1

    return result



print(binarySubstring('00110011'))