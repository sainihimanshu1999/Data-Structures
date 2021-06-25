'''finding the size of minimum set of numbers to remove such that my original array becomes half of the size'''

from collections import Counter
def reduce(arr):
    n = len(arr)//2

    count = Counter(arr)

    count = sorted(c.values())
    
    result = 0
    size = 0

    while size<n:
        x = count.pop()
        size+=x
        result+=1
    return result
