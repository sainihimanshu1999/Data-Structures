def reverseDLL(head):
    #return head after reversing
    t = None
    curr = head
    while curr:
        #flipping the orientation of next and previous links
        t = curr.prev
        curr.prev = curr.next
        curr.next = t
        curr = curr.prev
    if t:
        #setting the head to the last element of the list
        head = t.prev
    return head
