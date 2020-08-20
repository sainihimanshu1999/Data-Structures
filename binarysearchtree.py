class TreeEmptyError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.child, x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild, x)
        else:
            print(x, ' is already present in the tree')
        return p

    def delete1(self):
        p = self.root
        par = None

        while p:
            if x == p.info:
                break
            par = p
            if x < p.info:
                p = p.lchild
            else:
                p = p.rchild

        if p == None:
            print(x, ' is not found')
            return

        # case 2 : find the inorder successor and it's parents

        if p.lchild and p.rchild:
            ps = p
            s = p.rchild

            while s.lchild:
                ps = s
                s = s.lchild
            p.info = s.info
            p = s
            par = ps

        # case B: one or no child
        if p.lchild:  # node to be deleted has the left child
            ch = p.lchild
        else:  # node to be deleted has the right child
            ch = p.rchild

        if par == None:  # node to be deleted is the root node
            self.root = ch
        elif p == par.lchild:
            par.lchild = ch
        else:
            par.rchild = ch

    def search(self, x):
        return self._search(self.root, x) is not None

    def _search(self, p, x):
        if p is None:
            return None  # key is not found because tree is empty
        if x < p.info:
            return self._search(p.lchid, x)  # for searching the left subtree
        if x > p.info:
            return self._search(p.rchild, x)  # for searching in right subtree
        return p  # key found

    def search1(self, x):  # iterative method to search the key into the binary search tree
        p = self.root:
        while p:
            if x < p.info:
                p = p.lchild  # moving to the left subtree
            elif x > p.info:
                p = p.rchild  # moving to the right subtree
            else:  # x found
                return True
        return False

    def min1(self):  # iterative method to find the minimum node in bst
        if self.is_empty():
            raise TreeEmptyError('Tree is empty')

        p = self.root
        while p.lchild:
            p = p.lchild
        return p.info

    def max1(self):  # iterative method to find the maximum node in bst
        if self.is_empty():
            raise TreeEmptyError('Tree is empty')
        p = self.root
        while p.rchild:
            p = p.rchild
        return p.info

    def min2(self):
        if self.is_empty():
            raise TreeEmptyError('Tree is empty')
        return self._min(self.root).info

    def _min(self, p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)

    def max2(self):
        if self.is_empty():
            raise TreeEmptyError('Tree is empty')
        return self._max(self.root).info

    def _max(self, p):
        if p.rchild is None:
            return p
        return self._max(p.rchild)

    def insert1(self, x):  # iterative method to add the node in the bst
        p = self.root
        par = None
        while p:
            par = p
            if x < p.info:
                p = p.lchild
            if x > p.info:
                p = p.rchild
            else:
                print(x, 'already present in the tree')

        temp = Node(x)
        if par == None:
            self.root = temp
        elif x < par.info:
            par.lchild = temp
        else:
            par.rchild = temp
