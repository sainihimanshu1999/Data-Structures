'''There are various method to do this, i would do this my dp memoization'''


from typing import NewType


def combinationSum(nums,target):
    count =0
    memo = {}

    def dp(nums,target,memo):
        if target in memo:
                return memo[target]
            
        else:
            count = 0
            
            for num in nums:
                if num<=target:
                    new_target = target-num
                    
                    if new_target == 0:
                        count+=1
                        continue
                    
                    count += dp(nums,new_target,memo)
                    
                    
                    
            memo[target] = count
                
            return count

    count = dp(nums,target,memo)
    return count


nums = [1,2,3]
target = 4

print(combinationSum(nums,target))