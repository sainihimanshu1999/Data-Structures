class EmptyStackError(Exception):
    pass


class StackFullError(Exception):
    pass


class Stack:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.items)

    def size(self):
        return self.count

    def push(self, x):
        if self.is_full():
            raise StackFullError('Stack is full, cannot push')

        self.items[self.count] = x
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty, cannot pop')
        x = self.items[self.count - 1]
        self.items[self.count-1] = None
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self.items[-1]

    def display(self):
        print(self.items)


# sstack = Stack()
# sstack.push(5)
# sstack.push(8)
# sstack.push(10)
# sstack.push(90)
# sstack.push(67)
# sstack.push(90)
# sstack.push(90)
# sstack.push(90)
# sstack.push(90)
# sstack.push(90)
# sstack.push(90)
# sstack.pop()
# sstack.is_empty()
# print(sstack.peek())
# print(sstack.size())
# sstack.display()
