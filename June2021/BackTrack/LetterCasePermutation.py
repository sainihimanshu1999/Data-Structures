'''letter case permutation, upper case and lower case'''

def letterCasePermutation(s):
    def dfs(i,string):
        nonlocal ans
        if i==len(s):
            ans.append(string)
            return 
        if s[i].isalpha():
            dfs(i+1,string +s[i].lower())
        dfs(i+1,string+s[i].lower())

    ans = []
    dfs(0,'')
    return ans
