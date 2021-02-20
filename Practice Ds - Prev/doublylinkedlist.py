class Node:
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class Doublelinkedlist(object):
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print('List is empty')
            return

        print('List is: ')
        p = self.start
        while p:
            print(p.info, " ", end='')
            p = p.next
        print()

    def prepend(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert__in_emptylist(self, data):
        temp = Node(data)
        self.start = temp

    def append(self, data):
        temp = Node(data)
        p = self.start
        while p.next:
            p = p.next
        p.next = temp
        temp.prev = p

    def insert_after(self, data, x):
        temp = Node(data)
        p = self.start
        while p:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x, ' is not present in the list')
        else:
            temp.prev = p
            temp.next = p.next
            if p.next:
                p.next.prev = temp  # it should not be done, when p is the last node
            p.next = temp

    def insert_before(self, data, x):
        if self.start is None:
            print('List is empty')
            return

        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = prev
            self.start = temp
            return

        p = self.start
        while p:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print(x, ' is not present in the list')
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):
        if self.start is None:  # list is empty
            return
        if self.start.next is None:
            self.start = None
            return  # list has only one node
        self.start = self.start.next
        self.start.prev = None

    # def delete_one_node(self, x):
    #     self.start = None

    def delete_node(self, x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start = None
        else:
            print(x, ' is not found')

        # deletion of the first node
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start.next
        while p.next:
            if p.info == x:
                break
            p = p.next

        if p.next:
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            if p.info == x:
                p.prev.next = None
            else:
                print(x, ' is not found')

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return

        p = self.start
        while p.next:
            p = p.next
        p.prev.next = None

    def reverse(self):
        if self.start is None:
            return

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2

        while p2:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1


llist = Doublelinkedlist()
llist.insert__in_emptylist(5)
llist.prepend(89)
llist.append(7)
llist.append(9)
llist.append(10)
llist.append(3)
llist.append(6)
llist.insert_after(33, 10)
llist.insert_before(22, 33)
llist.delete_first_node()
llist.delete_last_node()
llist.delete_node(10)
llist.reverse()
llist.display_list()
