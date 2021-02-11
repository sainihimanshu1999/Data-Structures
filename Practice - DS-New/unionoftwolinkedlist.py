def union(head1,head2):
    s = set()
    while head1!=None:
        s.add(head1.data)
        head1 = head1.next
    while head2!=None:
        s.add(head2.data)
        head2 = head2.next
    arr = list(s)
    arr.sort()
    ret = Node(arr[0])
    t = ret
    for i in range(1,len(arr)):
        ret.next = Node(arr[i])
        ret = ret.next
    return ret