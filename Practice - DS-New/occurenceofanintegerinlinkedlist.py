"""  Return the no. of times search_for value is there in a linked list.
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def count(head, search_for):
    count = 0
    while(head):
        if(head.data==search_for):
            count += 1
        head= head.next
    return count