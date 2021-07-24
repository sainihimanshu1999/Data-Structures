'''We have the max sum of adjancent houses'''


def houseRobber(houses):
    prev=curr=0

    for house in houses:
        temp = prev
        prev = curr
        curr = max(house+temp,prev)

    return curr



nums = [1,2,3,1]
print(houseRobber(nums))