'''
In this question we have to find the k-concatenation sum of the array, we are going to use kadane's algorithm, 
if k == 1 we can easliy find max_sub array sum but it has been repeated more than 1 time we can check kadane's algorithm
on just the two array and then multply k-2 by sum of array
'''


def kcontcatenation(arr,k):
    def kadane(sub_arr):
        current_sum = 0
        max_endsum = 0

        for i in range(len(sub_arr)):
            current_sum = max(0,current_sum+sub_arr[i])
            max_endsum = max(max_endsum,current_sum)

        return max_endsum

    if not arr:
        return 0

    sumi = sum(arr)

    if k == 1:
        return max(0,kadane(arr))%(10**9+7)

    else:
        return max(0,(k-2)*max(sumi,0)+kadane(arr+arr))%(10**9+7)


arr = rr = [1,-2,1]
k = 5
print(kcontcatenation(arr,k))