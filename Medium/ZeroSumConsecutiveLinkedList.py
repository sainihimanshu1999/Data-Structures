'''We will going to use prefix sum in this questoin'''


def zeroSum(head):
    dummy = ListNode(0)
    dummy.next = head
    dic = {}
    prefix = 0

    while head:
        prefix += head.val
        dic[prefix] = head
        head = head.next

    head = dummy
    prefix = 0

    while head:
        prefix += head.val
        head.next = dic[prefix].next
        head = head.next
    
    return dummy.next
        