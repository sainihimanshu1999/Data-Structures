# def sortList(head)
#     prev = head  
#         curr = head.next
            
#             # Traverse list  
#         while(curr != None):  
#             if(curr.data < prev.data): 
#                 prev.next = curr.next
#                 curr.next = head  
#                 head = curr 
#                 curr = prev  
                
#             else: 
#                 prev = curr 
            
#             curr = curr.next
#         return head  

'''this above solution is absolutely correct but it did not work in gfg console that's why next one is used'''
def sortList(head): 
    l = []
    while head:
        l.append(head.data)
        head = head.next
    l1 = sorted(l)
    ll.head = None
    for i in l1:
        ll.append(i)
    return ll