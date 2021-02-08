def update(llist, p):
    if p == 0:
        return
    current = llist.head
    
    count = 1
    while count<p and current!=None:
        current = current.next
        count+=1
        
    if current == None:
        return
    
    Nthnode = current
    
    while current.next!=None:
        current = current.next
    
    current.next = llist.head
    llist.head.prev = current
    llist.head = Nthnode.next
    llist.head.prev = None
    Nthnode.next = None
    
    return llist