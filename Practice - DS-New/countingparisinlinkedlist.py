'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def countPair(h1,h2,n1,n2,x):
    '''
    h1:  head of linkedList 1
    h2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:   len of linkedList 1
    X:   given sum
    '''
    count = 0
    a = h1
    while(a!=None):
        b = h2
        while(b!=None):
            if((a.data+b.data)==x):
                count +=1
            b = b.next
        a = a.next
    return count