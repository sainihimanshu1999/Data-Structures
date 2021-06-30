'''we are given a sequence which has additive sequence 1 1 2 3 5 8'''

def additiveSequence(s):

    def dfs(num1,num2,string):
        if len(num1)>1 and num1[0]=='0':
                return False
            
        if len(num2)>1 and num2[0]=='0':
            return False
        
        if not string:
            return True
        
        num3 = str(int(num1)+int(num2))
        
        if string.startswith(num3):
            return dfs(num2,num3,string[len(num3):])
        else:
            return False


    for i in range(len(s)-2):
        for j in range(i+1,len(s)-1):
            if dfs(s[:i+1],s[i+1:j+1],s[j+1:]):
                return True
    return False


s = "199100199"
print(additiveSequence(s))