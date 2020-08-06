'''
Easy way when precision is not required
'''
# s = ''.join(map(str, A))
# print(int(s) + 1)


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


B = [1, 4, 9]
C = [9, 9, 9]

print(plus_one(B))
print(plus_one(C))
