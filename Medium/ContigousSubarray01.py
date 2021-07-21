'''In this question we have to find the maximum length contigous subarray which have equal number of zeroes and ones'''


def contigousSubarray(nums):
    count = 0
    dic = {0:-1}
    max_length = 0

    for i,num in enumerate(nums):
        if num == 0:
            count -=1

        else:
            count +=1

        if count in dic:
            max_length = max(max_length,i-dic[count])