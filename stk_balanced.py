from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_balanced(string):
    s = Stack()
    bal = True
    index = 0

    while index<len(string) and bal:
        paren = string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty:
                bal = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    bal = False
        index +=1
    if s.is_empty() and bal:
        return True
    else:
        return False
    
    


print(is_balanced("()"))

