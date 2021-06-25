'''
baic tracking of two largest number in the array and then finding thier product according to our need
'''

def maxProd(nums):
    a=b=-1
    for num in nums:
        if num>a:
            a,b = num,a
        elif num>b:
            b=num
    return (a-1)*(b-1)



nums = [1,5,4,5]
print(maxProd(nums))