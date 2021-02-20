class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not there")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_node(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # print(prev_1.data)
        # print(curr_1.data)

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head


# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()

    def remove_duplicates(self):
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
            else:
                # have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        '''
        Method to calculate the length of the list
        '''
        total_len = self.len_iterative()
        print(total_len)

        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def pointer_calculation(self, n):
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1

        if not q:
            print(str(n) + 'is greater than number of nodes')

        while p and q:
            p = p.next
            q = q.next
        return p.data

    def occurence_it(self, data):
        count = 0
        cur = self.head

        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def occurence_rec(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.occurence_rec(node.next, data)
        else:
            return self.occurence_rec(node.next, data)

    '''
    Palindrome Problem
    '''

    def is_palimdrome(self):
        # Method 1
        # s = ''
        # p = self.head

        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]

        # Method 2 using stack prperties in the list
        # s = []
        # p = self.head

        # while p:
        #     s.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True
        # Method 3 using two pointers P and Q
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = (prev[-1])
        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def tail_to_head(self):
        last = self.head
        secondlast = None

        while last.next:
            secondlast = last
            last = last.next
        last.next = self.head
        secondlast.next = None
        self.head = last

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()


llist1 = LinkedList()
llist1.append(7)
llist1.append(0)
llist1.append(0)

llist2 = LinkedList()
llist2.append(2)
llist2.append(0)
llist2.append(0)

llist1.sum_two_lists(llist2)

# llist2 = LinkedList()
# llist2.append('H')
# llist2.append('E')
# llist2.append('L')
# llist2.append('L')
# llist2.append('O')

# llist2.print_list()
# llist2.tail_to_head()
# print('\n')
# llist2.print_list()

# llist1 = LinkedList()
# llist1.append('R')
# llist1.append('A')
# llist1.append('D')
# llist1.append('A')
# llist1.append('R')

# llist2 = LinkedList()
# llist2.append('H')
# llist2.append('E')
# llist2.append('L')
# llist2.append('L')
# llist2.append('O')

# print(llist1.is_palimdrome())
# print(llist2.is_palimdrome())


# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(1)
# llist.append(3)
# llist.append(1)
# llist.append(3)

# print(llist.occurence_rec(llist.head, 1))

# llist = LinkedList()
# llist.append('A')
# llist.append('B')
# llist.append('C')
# llist.append('D')
# llist.append('E')

# print(llist.pointer_calculation(2))


# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)
# llist.remove_duplicates()
# llist.print_list()
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.append("H")
# llist.append("S")
# llist.swap_node('A', 'C')
# # llist.insert_after_node(llist.head.next, "E")
# llist.append("E")
# llist.delete_node_at_pos(2)
# print(llist.len_iterative())
# llist.reverse_iterative()
# print(llist.len_recursive(llist.head))
# llist.print_list()
