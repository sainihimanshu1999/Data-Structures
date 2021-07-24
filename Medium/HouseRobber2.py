'''This question is same as house robber one as but in this questions houses are in circle'''

def houseRobber(houses):

    def stolen(nums):
        prev=curr=0

        for num in nums:
            temp = prev 
            prev = curr
            curr = max(num+temp,prev)
        
        return curr

    if not houses:
        return 0

    if len(houses) == 1:
        return houses[0]

    return max(stolen(houses[1:]),stolen(houses[:-1]))