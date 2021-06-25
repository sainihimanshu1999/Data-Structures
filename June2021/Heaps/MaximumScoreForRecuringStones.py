'''
using greedy algorithm
'''

def maximumScore(a,b,c):
    word = [a,b,c]
    word.sort()

    result = 0 
    
    while word[1]:
        result += 1
        word[1] -= 1
        word[2] -= 1
        word.sort()
    return result


a = 2
b = 4
c = 6

print(maximumScore(a,b,c))