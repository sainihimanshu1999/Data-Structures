def isPalindromeUtil(string): 
    return (string == string[::-1]) 
  
    # Returns true if string formed by linked list is  
    # palindrome 
def compute(head): 
    node = head 
    temp = [] 
    while (node is not None): 
        temp.append(node.data) 
        node = node.next
    string = "".join(temp) 
    return isPalindromeUtil(string) 