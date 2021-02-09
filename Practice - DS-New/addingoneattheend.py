def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt  = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    head = prev
    return head




def addOne(head):
    head = reverseList(head)
    k = head
    carry = 0
    prev = None
    head.data += 1
    while(head != None) and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next
 
    if carry > 0:
        prev.next = Node(carry)
    return reverseList(k)
