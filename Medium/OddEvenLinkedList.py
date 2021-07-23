'''moving odd indices element and even indices element together'''


def oddEven(head):
    if not head:
        return head

    odd = head
    even = head.next
    eHead = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = eHead

    return head