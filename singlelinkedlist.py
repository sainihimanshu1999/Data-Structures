class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList():
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print('List is empty')
            return
        else:
            print('List is :')
            p = self.start
            while p is not None:
                print(p.info, " ", end=' ')
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print('Number of nodes in the list = ', n)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, "is at position", position)
                return True
            position += 1
            p = p.link
        else:
            print(x, ' is not found in the list')
            return False

    def prepend(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def append(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input('Enter the number of node: '))
        if n == 0:
            return
        for i in range(n):
            data = int(input('Enter the value of element to be inserted: '))
            self.append(data)

    def insert_after(self, data, x):
        p = self.start
        while p:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x, ' not present in the list')
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # if the list is empty
        if self.start is None:
            print('List is empty')
            return
        # if x is in the first node and it has to be added before the first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        # finding the reference to the predecessor of the node containig x
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(x, ' not present in the list')
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        # at the first node
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        # if it s not to be inserted at the start
        p = self.start
        i = 1
        # finding the reference to the k-1 node
        while i < k-1 and p:
            p = p.link
            i += 1

        if p is None:
            print('You can insert upto position', i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    # deleting the node at the specific position
    def delete_node(self, x):
        if self.start is None:
            print('List is empty')
            return

        # deletion of the first Node
        if self.start.info == x:
            self.start = self.start.link
            return

        # deletion between or in the end of the list
        p = self.start
        while p.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print('Element', x, 'not in the list')
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        else:
            self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link:
            p = p.link
        p.link = None

    def reverse_list(self):
        prev = None
        p = self.start
        while p:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubblesort_data(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubblesort_link(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.link
            end = p

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list

    def _merge1(self, p1, p2):
        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link
        pM = startM

        while p1 and p2:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

        # if second list is finished and the elements in the first list are remaining
            while p1:
                pM.link = Node(p1.info)
                p1 = p1.link
                pM = pM.link

            # if the first list has finished and the elements in second lists are remaining
            while p2:
                pM.link = Node(p2.info)
                p2 = p2.link
                pM = pM.link

            return startM

    def merge2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):
        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link
        pM = startM

        while p1 and p2:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1
        return startM

    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)

    def _merge_sort_rec(self, list_start):
        # if the list is empty and have only one element
        if list_start is None or list_start.link is None:
            return list_start

        # if more than one element
        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(star1, start2)
        return startM

    def _divide_list(self, p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = q.link
            q = q.link.link
        start2 = p.link
        p.link = None
        return start2

    def insert_cycle(self, x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None

        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link

        if px is not None:
            prev.link = px
        else:
            print(x, 'not present in the list')

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None

        slowR = self.start
        fastR = self.start

        while fastR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None

    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return
        print('Node at which the cycle is detected is', c.info)

        p = c
        q = c
        len_cycle = 0

        while True:
            len_cycle += 1
            q = q.link
            if p == q:
                break

        print('length of the cycle is: ', len_cycle)

        len_rem_list = 0
        p = self.start
        while p != q:
            len_rem_list += 1
            p = p.link
            q = q.link

        print('Number of nodes not included in the cycle are: ', len_rem_list)
        length_of_list = len_cycle + len_rem_list
        print('Length of the total list: ', length_of_list)

        p = self.start
        for i in range(length_of_list - 1):
            p = p.link
        p.link = None


llist = SingleLinkedList()
llist.append(5)
llist.append(20)
llist.append(8)
llist.append(12)
llist.append(20)
llist.append(49)
llist.append(60)
llist.append(87)

# llist2 = SingleLinkedList()
# llist2.append(7)
# llist2.append(11)
# llist2.append(14)
# llist2.append(18)
# llist.insert_before(14, 5)
# llist.insert_after(25, 14)
# llist.insert_at_position(75, 3)
# # llist.delete_node(5)
# # llist.delete_last_node()
# # llist.reverse_list()
# # llist.bubblesort_data()
# llist.bubblesort_link()
# # `llist.merge1(llist2)`
# llist.merge_sort()
llist.insert_cycle(20)
llist.remove_cycle()
llist.display_list()
