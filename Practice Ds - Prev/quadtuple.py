def quadtuple(A, sum):
    # we create in an empty dict
    # key: sum of a pair of elements in the list
    # value: list storing the index of every pair having that sum
    n = len(A)
    dict = {}

    # consider each element except last element
    for i in range(n-1):
        # start for ith element till last element
        for j in range(i+1, n):
            # calculate remaining sum
            val = sum - (A[i] + A[j])

            # if remaining sum is found in the dictionary, we have found a Quadruplet
            if val in dict:
                # check every pair having sum equal to remaining sum
                for pair in dict[val]:
                    x, y = pair

                    # if quadruplet don't overlap print it and return True
                    if (x != i and x != j) and (y != i and y != j):
                        print(
                            'Qudaruplet Found', (A[i], A[j], A[x], A[y]))
                        return True
            # Inserting the current pair in the dictionary
            dict.setdefault(A[i]+A[j], []).append((i, j))

    # return false if Quadruplets don't exists
    return False


A = [2, 7, 4, 0, 9, 5, 1, 3]
sum = 20
quadtuple(A, sum)
