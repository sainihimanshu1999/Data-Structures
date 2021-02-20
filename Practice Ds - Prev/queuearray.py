class EmptyQueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def is_empty(self):
        return self.front == len(self.items)

    def size(self):
        return len(self.items) - self.front

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('This list is empty')
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = self.front + 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items[self.front]

    def display(self):
        print(self.items)


qq = Queue()
qq.enqueue(2)
qq.enqueue(5)
qq.enqueue(9)
qq.enqueue(11)
qq.enqueue(34)
print(qq.size())
# qq.dequeue()
qq.display()
