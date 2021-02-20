class EmptyStackError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):
        if self.is_empty():
            return 0

        count = 0
        p = self.top
        while p:
            count += 1
            p = p.link
        return count

    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        popped = self.top.info
        self.top = self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self.top.info

    def display(self):
        if self.is_empty():
            print('stack is empty')
            return

        print('Stack is: ')
        p = self.top
        while p:
            print(p.info, ' ')
            p = p.link


sstack = Stack()
sstack.push(5)
sstack.push(6)
sstack.push(58)
sstack.push(12)
sstack.push(43)
sstack.push(00)
# sstack.pop()
print(sstack.is_empty())
print(sstack.size())
print(sstack.peek())
sstack.display()
