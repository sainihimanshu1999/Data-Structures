def quick_sort(a):
    sort(a, 0, len(a)-1)


def sort(a, low, up):
    if low >= up:
        return
    p = partition(a, low, up)
    sort(a, low, p-1)
    sort(a, p+1, up)


def partition(a, low, up):
    pivot = a[low]
    i = low + 1
    j = up

    while i <= j:
        while a[i] < pivot and i < up:
            i += 1
        while a[j] > pivot:
            j -= 1

        if i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
            j -= 1
        else:
            break

    a[low] = a[j]
    a[j] = pivot

    return j


a = [12, 54, 34, 78, 5, 90, 12, 45, 87]
quick_sort(a)
print(a)
