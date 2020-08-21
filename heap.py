class HeadEmptyError(Exception):
    pass


class Heap:
    def __init__(self, maxSize=10):
        self.a = [None]*maxSize
        self.n = 0
        self.a[0] = 9999

    def insert(self, value):
        self.n += 1
        self.a[self.n] = value
        self.restore_up(self.h)

    def restore_up(self, i):
        k = self.a[i]
        iparent = i//2

        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i = iparent
            iparent = i//2
        self.a[i] = k

    def delete_root(self):
        if self.n == 0:
            raise HeadEmptyError('Head is empty')

        max_value = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -= 1
        self.restore_down(1)
        return max_value

    def restore_down(self, i):
        k = self.a[i]
        lchild = 2*1
        rchild = lchild+1

        while rchild <= self.n:
            if k > self.a[lchild] and k >= self.a[rchild]:
                self.a[i] = k
                return
            else:
                if self.a[lchild] > self.a[rchild]:
                    self.a[i] = self.a[lchild]
                    i = lchild
                else:
                    self.a[i] = self.a[rchild]
                    i = rchild

            lchild = 2*1
            rchild = lchild + 1

        if lchild == self.n and k < self.a[lchild]:
            self.a[i] = self.a[lchild]
            i = lchild
        self.a[i] = k

    def build_heap_top_down(a, n):
        for i in range(2, n+1):
            restore_up(1, a)

    def build_heap_bottom_up(a, n):
        i = n//2
        while i >= 1:
            restore_down(i, a, n)
            i = i-1
