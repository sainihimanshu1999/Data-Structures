def findnthroot(x, n):
    # boundary values
    x = float(x)
    n = int(n)

    if(x >= 0 and x <= 1):
        low = x
        high = 1
    else:
        low = 1
        high = x

    # this variable is used for taking the approximations of the answer
    epsi = 0.0001

    # starting the binary search
    guess = (low+high)/2
    while abs(guess**n-x) >= epsi:
        if guess**n > x:
            high = guess
        else:
            low = guess
        guess = (low+high)/2
    print(round(guess, 4))


x = 5
n = 2
findnthroot(x, n)
