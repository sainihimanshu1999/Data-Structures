'''Insertion sort basically iterates consuminh one input element each repetation and growing sorted one out, at each iteration
, iteration set removes one element from the input data, find the loaction it belongs within the sorted set'''



def linkedListInsertionsort(head):

    dummy = ListNode(0)


    dummy.next = head

    while head and head.next:

        if head.val>head.next.val:
            node_to_insert = head.next


            node_to_insert_prev = dummy

            if node_to_insert.next.val < node_to_insert.val:
                node_to_insert_prev = node_to_insert_prev.next


            head.next = node_to_insert.next
            node_to_insert.next = head
            node_to_insert_prev.next = node_to_insert

        else:
            head = head.next


    return dummy.next
    

    