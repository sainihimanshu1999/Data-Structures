n=int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
while left < right:
    while(arr[left] % 2 == 0 and left < right):
        left = left + 1
    while(arr[right] % 2 == 1 and left < right):
        right = right - 1
    if (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left = left + 1
        right = right - 1
        
for i in range (0, n):
    print(arr[i], end = ' ')
