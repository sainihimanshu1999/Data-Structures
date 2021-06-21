'''
we have to keep in mind that sum(s[i:j])%k==0 is equal to sum(s[:j])%k==sum(s[:i])%k so we just need to keep track
of sum(nums[:i])%k and i and if we found i' where above conditon satisfy and i-i>1 then we found our answer
'''

def conitnousSubarray(nums,k):
    dic = {0:-1}
    sumi = 0

    for i in range(len(nums)):
        sumi = sumi+nums[i]

        if k!=0:
            sumi = sumi%k

        if sumi in dic:
            if (i-dic[sumi])>1:
                return True
        else:
            dic[sumi] = i
    return False

