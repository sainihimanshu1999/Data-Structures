'''This is an easy question but we have to use basic logic or we can say it is hit and trial'''


def countBits(num):
    result = [0]
    while len(result)<=num:
        result += [i+1 for i in result]

    return result[:num+1]
