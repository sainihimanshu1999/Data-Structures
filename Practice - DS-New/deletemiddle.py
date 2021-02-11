def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    m  = middle(head)
    prev = head
    curr = head
    while curr!=None and curr.data!=m:
        prev = curr
        curr = curr.next
    
    prev.next = curr.next
    curr = None
    return head
            
    
    
    #code here
def middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
    