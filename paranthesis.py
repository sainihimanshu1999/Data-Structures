from stackarray import Stack


def paran(expr):

    st = Stack()

    for ch in expr:
        if ch in '({[':
            st.push(ch)
        if ch in ')}]':
            if st.is_empty():
                print('Right paranthesis is more than the Left ones')
                return False
            else:
                char = st.pop()
                if not match_parantheses(char, ch):
                    print('Mismatched paranthese are', char, 'and', ch)
    if st.is_empty():
        print('Balanced Parantheses')
        return True
    else:
        print('Left parantheses are more the right ones')
        return False


def match_parantheses(leftp, rightp):
    if leftp == '[' and rightp == ']':
        return True
    if leftp == '(' and rightp == ')':
        return True
    if leftp == '{' and rightp == '}':
        return True
    return False


while True:
    print("Enter an expression: ", end=" ")
    expression = input()
    if expression == 'q':
        break
    if paran(expression):
        print('Yo')
    else:
        print('No')
