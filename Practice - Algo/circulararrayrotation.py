#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    if k > len(a):
        k = k % len(a)
    k = len(a) - k
    a = a[k:] + a[:k]
    return [a[i] for i in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



'''
Lesser Time Complexity Solution


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    
    lst = [0]*(n+1)

    for _ in range(m):
        a,b,k = (map (int, input().rstrip().split()))
        lst[a-1] +=k
        if b<=len(lst):
            lst[b] -= k
    
    maxx = summ = 0
    for i in lst:
        summ += i
        if summ>maxx:
            maxx = summ
        
    fptr.write(str(maxx) + '\n')

    fptr.close()

'''