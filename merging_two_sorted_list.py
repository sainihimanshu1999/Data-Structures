def merge(a1, a2, temp):
    i = 0
    j = 0
    k = 0
    n1 = len(a1)
    n2 = len(a2)

    while i <= n1-1 and j <= n2-1:
        if a1[i] < a2[j]:
            temp = a1[i]
            i += 1
        else:
            temp = a2[j]
            j += 1
        k += 1

    # if a2 is finished
    while i <= n1-1:
        temp[k] = a1[i]
        i += 1
        k += 1

    # if a1 is finished
    while j <= n2-1:
        temp[k] = a2[j]
        j += 1
        k += 1


a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = [11, 22, 33, 44, 55, 66, 77, 88]
temp = [None]*(len(a1)+len(a2))

merge(a1, a2, temp)
print(temp)
