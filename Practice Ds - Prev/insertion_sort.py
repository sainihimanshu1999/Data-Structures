def insertion_sort(a):
    for i in range(len(a)):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp


x = [89, 34, 12, 45, 7, 5, 44, 22]

insertion_sort(x)
print(x)
