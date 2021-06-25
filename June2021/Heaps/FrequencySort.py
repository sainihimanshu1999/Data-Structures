'''Frequency sort id done using dictionary and there are various ways to sort the dictionary element it was just an
intutive soltuion'''

from collections import Counter
#import collections
def frequencySort(s):
    count = Counter(s)

    freq = sorted(count.items(),key=lambda x:x[1],reverse=True)

    return ''.join(x[0]*x[1] for x in freq)


s = 'tree'
print(frequencySort(s))
