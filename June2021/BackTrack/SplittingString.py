'''we have to split the string and order them in decending order and if that is possible return true'''


def splittingString(s):
    result = False

    def dfs(num,string,level):
        nonlocal result
            
        if num<0:
            return 
        
        if len(string) == 0 or (num == int(string) and level>0):
            result = True 
            
        for j in range(1,len(string)):
            if num == int(string[:j]):
                dfs(num-1,string[j:],level+1)

    for i in range(1,len(s)):
        dfs(int(s[:i]),s,0)

    return result


s = "050043"
print(splittingString(s))