'''It's a simple question involving xor of the number'''

def xorOperation(n,start):
    result= start
    for i in range(1,n):
        result = result^(start+2*i)

    return result