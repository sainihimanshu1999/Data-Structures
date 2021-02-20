def array_advance(A):
    furthest_reached = 0
    last_indx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_indx:
        furthest_reached = max(furthest_reached, A[i]+i)
        i += 1

    return furthest_reached >= last_indx


B = [3, 0, 0, 0, 2, 0, 1]
print(array_advance(B))
