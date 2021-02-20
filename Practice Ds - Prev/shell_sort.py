def shell_sort(a):
    h = int(input('Enter increment odd value: '))
    while h >= 1:
        for i in range(h, len(a)):
            temp = a[i]
            j = i - h
            while j >= 0 and a[j] > temp:
                a[j+h] = a[j]
                j = j-h
            a[j+h] = temp
        h = h-2
