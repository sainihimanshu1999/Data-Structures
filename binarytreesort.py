class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None


class BinarySearchTree:
    def __init__(self):
        self.root == None

    def is_empty(self):
        return self.root == None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        else:
            p.rchild = self._insert(p.rchild, x)
        return p

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info, ' ')
        self._inorder(p.rchild)


tt = BinarySearchTree()
tt.insert(23)
tt.insert(46)
tt.insert(59)
tt.insert(89)
tt.insert(32)
tt.insert(14)
tt.insert(20)
print(tt)
