'''
level max + level min  curr /2 = label , end - (curr-start), curr-start will give the index of array if the tree has
not been inverted and subtracting this from end gives us index in inverted tree
'''

def zigZag(label):
    node_count = 1
    level = 1
    result = []

    while label>=node_count*2:
        node_count *= 2
        level +=1

    #print(node_count,level)

    while label!=0:
        result.append(label)
        level_max = 2**(level)-1
        level_min = 2**(level-1)
        label = int((level_max+level_min-label)/2)
        level -=1
    
    return result[::-1]


print(zigZag(14))

