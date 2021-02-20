def binary2decimal(n):
    num = n
    dec = 0

    # intializing the base that is 2^0
    base = 1

    temp = num
    while(temp):
        lastdigit = temp % 10
        temp = int(temp/10)

        dec += lastdigit*base
        base = base*2
    print(dec)
    return


n = 101010101
binary2decimal(n)
