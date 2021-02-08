def getMiddle(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    return slow

def merge(left, right):
    if not left or not right: return right if not left else left
    if left.data <= right.data:
        merged, left.next = left, merge(left.next, right)
    else: merged, right.next = right, merge(left, right.next)
    return merged

def mergeSort(head):
    if not head or not head.next: return head
    middle = getMiddle(head)
    right, middle.next = middle.next, None
    return merge(mergeSort(head), mergeSort(right))