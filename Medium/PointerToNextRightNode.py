'''In this question we ahve to point next pointers to the right node of the tree and then to null'''


def nextPointer(root):
    node = root

    while node:
        curr = dummy = Node(0)
        while node:
            if node.left:
                curr.next = node.left
                curr = curr.next

            if node.right:
                curr.next = node.right
                curr = curr.next

            node = node.next

        node = dummy.next


    return root