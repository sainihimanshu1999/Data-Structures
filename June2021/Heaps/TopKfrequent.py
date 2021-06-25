'''
top k frequent elements
'''

from _typeshed import ReadableBuffer
from collections import Counter

def frequent(nums,k):
    freq = Counter(nums)

    result = []

    result = sorted(freq,key=freq.get,reverse=True)

    return result[:k]