'''all possibilities of the string, or all the numbers of string possibility'''


def numPossibilities(s):
    result = set()

    def dfs(path,string):
        if path not in result:
            if path:
                result.add(path)

            for i in range(len(string)):
                dfs(path+string[i],string[:i]+string[i+1:])

    dfs('',s)
    return len(result)


s = 'ABB'
print(numPossibilities(s))