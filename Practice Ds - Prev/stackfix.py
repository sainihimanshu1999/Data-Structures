from stackarray import Stack


def infix_to_postfix(infix):
    postfix = ''
    st = Stack()

    for symbol in infix:
        if symbol == ' ' or symbol == '/t':  # for ignoring blank spaces
            continue
        if symbol == '(':
            st.push(symbol)
        elif symbol == ')':
            next = st.pop()
            while next != '(':
                postfix += next
                next = st.pop()
        elif symbol in '+-*/%^':
            while not st.is_empty() and precedence(st.peek()) >= precedence(symbol):
                postfix = postfix + st.pop()
            st.push(symbol)
        else:  # for the operands
            postfix += symbol

    while not st.is_empty():
        postfix += st.pop()
    return postfix


def precedence(symbol):
    if symbol == '(':
        return 0
    elif symbol == '+-':
        return 1
    elif symbol == '*/%':
        return 2
    elif symbol == '^':
        return 3
    else:
        return 0


def evaluate(postfix):
    st = Stack()

    for symbol in postfix:
        if symbol.isdigit():
            st.push(int(symbol))
        else:
            x = st.pop()
            y = st.pop()

            if symbol == '+':
                st.push(y+x)
            elif symbol == '-':
                st.push(y-x)
            elif symbol == '*':
                st.push(y*x)
            elif symbol == '/':
                st.push(y/x)
            elif symbol == '%':
                st.push(y % x)
            elif symbol == '^':
                st.push(y**x)

        return st.pop()


print('Enter input: ')
expression = input()
postfix = infix_to_postfix(expression)
print('Postfix equation: ', postfix)
