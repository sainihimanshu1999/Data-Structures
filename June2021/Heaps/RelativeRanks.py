'''
This is easily done by the use of dictionary
'''

def ranks(score):
    newscore = sorted(score,reverse=True)
    dic = {}

    l = len(newscore)

    dic[newscore[0]] = 'Gold Medal'

    if l>1:
        dic[newscore[1]] = 'Silver Medal'

    if l>2:
        dic[newscore[2]] = 'Bronze Medal'

    for i in range(3,l):
        dic[newscore[i]] = str(i+1)

    res = [dic[k] for k in score]

    return res

score = [10,3,8,9,4]
print(ranks(score))

