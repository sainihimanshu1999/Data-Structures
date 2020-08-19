class EmptyQueueError(Exception):
    pass


class Node:
    def __init__(self, value, pr):
        self.info = value
        self.priority = pr
        self.link = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, data, data_priority):
        temp = Node(data, data_priority)

        # if the queue is empty or element to be added has priority more than first element
        if self.is_empty() or data_priority <= self.front.priority:
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link != None and p.link.priority <= data_priority:
                p = p.link
            temp.link = p.link
            p.link = temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        x = self.front.info
        self.front = self.front.link
        return x

    def is_empty(self):
        return self.front == None

    def display(self):
        if self.is_empty():
            print('Queue is empty')
            return

        print('Queue is: ')
        p = self.front
        while p:
            print(p.info, " ", p.priority)
            p = p.link
        print()

    def size(self):
        n = 0
        p = self.front
        while p:
            n += 1
            p = p.link
        return(n)

    def size(self):
        n = 0
        p = self.front
        while p:
            n += 1
            p = p.link
        return n


pq = PriorityQueue()
pq.enqueue(3, 1)
pq.enqueue(5, 2)
pq.enqueue(9, 4)
pq.enqueue(13, 6)
pq.enqueue(30, 5)
pq.enqueue(21, 3)
# pq.dequeue()
print(pq.size())
pq.display()
