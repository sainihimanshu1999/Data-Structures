def heap_sort(a, n):
    build_heap_bottom_up(a, n)
    while n > 1:
        maxValue = a[1]
        a[1] = a[n]
        a[n] = maxValue
        n = n-1
        restore_down(a, n)


def build_heap_bottom_up(a, n):
    i = n//2
    while i >= 1:
        restore_down(i, a, n)
        i = i-1


def restore_down(i, a, n):
    k = a[i]
    lchild = 2 * 1
    rchild = lchild + 1

    while rchild <= n:
        if k >= a[lchild] and k >= a[rchild]:
            a[i] = k
            return
        elif a[lchild] > a[rchild]:
            a[i] = a[lchild]
            i = lchild
        else:
            a[i] = a[rchild]
            i = rchild

        lchild = 2 * i
        rchild = lchild + 1

    # if number of nodes of given
    if lchild == n and k <= a[lchild]:
        a[i] = a[lchild]
        i = lchild
    a[i] = k
