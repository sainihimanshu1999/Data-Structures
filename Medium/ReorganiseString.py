'''Reorganise string using heaps, we store frequency in the heaps and then pop out one by one'''

from heapq import *

def reorganiseString(string):
    if not string:
        return ''

    dic = {}
    for char in string:
        dic[char] = dic.get(char,0)+1
    
    heap = []

    for char in dic:
        heappush(heap,(-dic[char],char))

    result = ''

    while len(heap)>1:
        f1,c1 = heappop(heap)
        f2,c2 = heappop(heap)

        result += c1
        result += c2

        if abs(f1)>1:
            heappush(heap,(f1+1,c1))

        if abs(f2)>1:
            heappush(heap,(f2+1,c2))

    
    if heap:
        f,c = heap[0]
        if abs(f)>1:
            return ''

        else:
            result +=c

    return result



s = "aab"
print(reorganiseString(s))

