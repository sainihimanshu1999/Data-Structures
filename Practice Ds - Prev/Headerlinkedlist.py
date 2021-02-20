class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None


class Headerlinkedlist(object):
    def __init__(self):
        self.start = Node(0)

    def display_list(self):
        if self.head.link = None
        print('List is empty')
        return

        p = self.head.link
        print('list is: ')
        while p:
            print(p.info, " ", end='')
            p = p.link
        print()

    def append(self, data):
        temp = Node(data)

        p = self.head
        while p.link:
            p = p.link
        p.link = temp

    def insert_before(self, data, x):
        p = self.head
        while p.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(x, ' is not present in the list')
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
