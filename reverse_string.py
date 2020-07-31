from stack import Stack


'''
How do we do it
1. Loop through the input string and push the characters onto the Stack
'''


def reverse_string(stack, a):
    for i in range(len(a)):
        stack.push(a[i])

    b = ''
    while not stack.is_empty():
        b += stack.pop()

    return b


stack = Stack()
a = 'HIMANSHU'

print(reverse_string(stack, a))


# print(a[::-1]) To directly reverse the string
