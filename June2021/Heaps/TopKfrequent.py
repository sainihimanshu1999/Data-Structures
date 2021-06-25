'''
top k frequent elements
'''

from _typeshed import ReadableBuffer
from collections import Counter

def frequent(nums):
    count = Counter(nums)

    result = []

    result = sorted(freq,key=freq.get,reverse=True)

    return result[:k]