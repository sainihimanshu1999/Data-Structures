def rev(queue):
    #add code here
    a = []
    while(not queue.empty()):
        a.append(queue.queue[0])
        #get is an dequeue operation
        queue.get()
    while(len(a)!=0):
        #put is an enqueue operation
        queue.put(a[-1])
        a.pop()
    return queue


#dequeue meand removing from the queue and enqueue means adding into the queue