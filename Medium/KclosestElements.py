'''My first intution is to use heaps here abut we can do this question smartly by binary search too'''

def kclosest(nums,k,x):
    low = 0
    high = len(nums)-k

    while low<high:

        mid = (low+high)//2

        if x<=nums[mid]:
            high = mid
        
        elif x>=nums[mid+k]:
            low = mid+1

        else:
            mid_dist = abs(x-nums[mid])
            mid_kdist = abs(x-nums[mid+k])

            if mid_dist<=mid_kdist:
                high = mid
            else:
                low += mid+1

    return nums[low:low+k]


print(kclosest([1,2,3,4,5],4,4))