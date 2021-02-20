class InvalidOperationException(Exception):
    pass


class studentRecord:
    def __init__(self, i, Name):
        self.studentId = i
        self.studentName = Name

    def get_student_id(self):
        return self.studentId

    def set_student_id(self, i):
        self.studentId = i

    def __str__(self):
        return str(self.studentId) + ' ' + studentName


class HashTable:
    def __init__(self, tableSize=11):
        self.m = tableSize
        seld.array = [None]*self.m
        self.n = 0

    def hash1(self, key):
        return(key % self.m)

    def insert(self, newRecord):
        key = newRecord.get_student_id()
        h = self.hash1(key)

        location = h

        for i in range(1, self.m):
            if self.array[location] is None or self.array[location].get_student_id() == -1:
                self.array[location] = newRecord
                self.n += 1
                return

            if self.array[location].get_student_id == key:
                raise InvalidOperationException('Duplicate Key')

            location = (h+i) % self.m

        print('table is full, this record cannot be inserted')

    def search(self, key):
        h = self.hash1(key)
        location = h

        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id() == key:
                return slef.array[location]

            location = (h+i) % self.m

        return None
