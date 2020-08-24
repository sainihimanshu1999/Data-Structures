def bubblesort(a):
    for x in range(len(a)-1, 0, -1):
        for j in range(x):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


A = [23, 56, 11, 68, 54, 89, 9]

bubblesort(A)
print(A)
