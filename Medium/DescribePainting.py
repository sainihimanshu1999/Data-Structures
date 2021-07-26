'''In this question we have to give mix color approach to this, we use sweep line apprach in this'''

from collections import defaultdict

def splitPainting(segments):

    dic =  defaultdict(int)

    for s,e,c in segments:
        dic[s] += c
        dic[e] -= c


    result = []

    prev,color = None,0

    for curr in sorted(dic):
        if prev is not None and color != 0 :
            result.append((prev,curr,color))


        color += dic[curr]
        prev = curr

    return result
