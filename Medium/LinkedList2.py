'''In this question we have to fins the cycle and then we have to find where the tail to linked list going as a cycle'''


def cycle2(head):

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


        if slow ==  fast:
            break


    if not fast or not fast.next:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow