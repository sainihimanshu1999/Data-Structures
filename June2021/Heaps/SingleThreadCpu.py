'''this works on shortest time first algorithm'''

from heapq import *

def singleThread(tasks):
    result = []
    heap = []
    tasks_new = sorted([(task[0],task[1],i) for i,task in tasks])
    i=0
    time= tasks_new[0][0]

    while len(result)<len(tasks_new):
        while i <len(tasks_new) and tasks_new[i][0]<=time:
            heappush(heap,(tasks_new[i][1],tasks_new[i][2]))
            i+=1

        if heap:
            process_time,index = heappop(heap)
            time += process_time
            result.append(index)

        elif i<len(tasks_new):
            time =  tasks_new[i][0]

    return result
    
