def compare(head1, head2):
    #return 1/-1/0
    count1 = 0
    count2 = 0
    while head1:
        head1 = head1.next
        count1 += 1
    while head2:
        head2 = head2.next
        count2 += 1
    if(count1 != count2):
        return('1')
    else:
        return('0')