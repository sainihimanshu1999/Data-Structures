'''we are giver first element, we just have to find the arr from which the encoded array is made'''

def enco(encoded,first):
    arr = [first]
    for num in encoded:
        arr.append(arr[-1]^num)

    return arr