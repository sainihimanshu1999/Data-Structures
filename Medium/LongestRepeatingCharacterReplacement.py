'''This question is done by using counters and by simple logic of sliding window'''

from collections import Counter

def longestRepeating(s,k):
    count = Counter()

    best,i =0,0

    for j in range(len(s)):
        count[s[j]]+=1
        best = max(best,count[s[j]])

        if best+k <j-i+1:
            i+=1
            count[s[i]] -=1
            #print(i)

    return len(s)-i


s = "AABABBA"
k = 1

print(longestRepeating(s,k))


