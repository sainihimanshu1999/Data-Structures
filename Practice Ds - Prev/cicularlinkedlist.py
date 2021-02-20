class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None


class Circularlinkedlist(object):
    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print('List is empty')
            return

        p = self.last.link

        while True:
            print(p.info, '', end='')
            p = p.link
            if p == self.last.link:
                break
            print()

    def prepend(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def append(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def delete_first_node(self):
        if self.last is None:
            return
        if self.last.link == self.last:
            self.last = None
            return
        self.last.link = self.last.link.link

    def delete_last_node(self):
        if self.last is None:
            return
        if self.last.link == self.last:
            self.last = None
            return

        p = self.last.link
        while p.link != self.last:
            p = p.link
        p.link = self.last.link
        self.last = p

    def delete_node(self, x):
        if self.last is None:
            return
        if self.last.link == self.last and self.last.link == x:
            self.last = None
            return
        if self.last.link.info == x:
            self.last.link = self.last.link.link
            return
        p = self.last.link
        while p.link != self.last.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link == self.last.link:
            print(x, 'not found in the list')
        else:
            p.link = p.link.link
            if self.last.info == x:
                self.last = p

    def concatenate(self, list2):
        if self.last is None:
            self.last = list2.last
            return

        if list2.last is None:
            return

        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last


llist = Circularlinkedlist()
llist.insert_in_empty_list(5)
llist.append(6)
llist.append(18)
llist.append(44)
llist.append(67)
llist.prepend(13)


llist2 = Circularlinkedlist()
llist2.insert_in_empty_list(5)
llist2.append(7)
llist2.append(28)
llist2.append(54)
llist2.append(77)
llist2.prepend(93)
# llist.delete_first_node()
# llist.delete_last_node()
# llist.delete_node(18)
llist.concatenate(llist2)
llist.display_list()
