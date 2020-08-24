def selection_sort(a):
    for i in range(len(a)-1):
        minIndex = i
        for j in range(i+1, len(a)):
            if(a[j] < a[minIndex]):
                minIndex = j

        if i != minIndex:
            a[i], a[minIndex] = a[minIndex], a[i]


x = [89, 65, 98, 32, 51, 11, 19]
selection_sort(x)
print(x)
