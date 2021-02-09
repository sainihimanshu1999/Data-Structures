def mergeResult(a,b):
    if (a == None and b == None ):
        return None
        
    res = None
    
    while(a!=None and b!=None):
        if(a.data <= b.data):
            temp = a.next
            a.next = res
            res = a
            a = temp
        else:
            temp = b.next
            b.next = res
            res = b
            b =temp
            
    while(a!=None):
        temp = a.next
        a.next = res
        res = a
        a = temp
    while(b!=None):
        temp = b.next
        b.next = res
        res = b
        b = temp
    
    return res