'''We use simple recurrsion in this question, but it was quite tricky'''


def binaryWatch(nums):

    def dfs(led,index,hours,minutes,n):
        if hours>=12 or minutes>=60:
            return 

        if not n:
            result.append(str(hours)+':'+'0'*(minutes<10)+str(minutes))
            return 

        if index<len(led):
            if index<=3:
                dfs(led,index+1,hours+led[index],minutes,n-1)
            else:
                dfs(led,index+1,hours,minutes+led[index],n-1)
            dfs(led,index+1,hours,minutes,n)

    led = [8,4,2,1,32,16,8,4,2,1]
    result = []
    dfs(led,0,0,0,nums)
    return result


turnedOn  = 1
print(binaryWatch(turnedOn))
