'''This is a dutch flag problem aka we use 3 pointers beg,mid,end '''


def sortColors(nums):
    beg,mid,end = 0,0,len(nums)-1

    while mid<=end:

        if nums[mid] == 0:
            nums[mid],nums[beg] = nums[beg],nums[mid]
            beg +=1
            mid +=1

        elif nums[mid] == 2:
            nums[mid],nums[end] = nums[end],nums[mid]
            end -=1

        else:
            mid +=1


    return nums


print(sortColors([1,2,0,0,1,2]))