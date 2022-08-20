import random, math
from tkinter.messagebox import NO

class HashTable:
    '''Set with repetitions (bag)'''
    def __init__(self):
        self.m = 128
        self.a = random.randint(0, 2**64 - 1)
        self._table = self.m * [None]
        self._iter_idx = None

    def insert(self, x):
        idx0 = self._hash(x)
        idx = idx0
        while self._table[idx] is not None:
            idx = (idx + 1) % self.m
            if idx == idx0:
                raise Exception('Hash Table overflow!')
        self._table[idx] = x

    def delete(self, idx):
        while True:
            self._table[idx] = None
            cur_idx = (idx + 1) % self.m
            while True:
                if self._table[cur_idx] is None:
                    return
                i = self._getIndexShift(self._table[cur_idx], idx)
                j = self._getIndexShift(self._table[cur_idx], cur_idx)
                if i < j:
                    break
                cur_idx += 1
            self._table[idx] = self._table[cur_idx]
            idx = cur_idx

    def _hash(self, k):
        # w = 64
        # l = int(math.log2(self.m))
        # h = (k*self.a % 2**w) >> (w-l)
        # return h
        return k % self.m

    def _getIndexShift(self, x, idx):
        return (idx - self._hash(x)) % self.m

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):
        if self._iter_idx is None or self._iter_idx == len(self._table):
            raise StopIteration

        while self._table[self._iter_idx] is None:
            self._iter_idx += 1
            if self._iter_idx == len(self._table):
                raise StopIteration

        self._iter_idx += 1
        return self._iter_idx-1, self._table[self._iter_idx-1]


#######################################################

if __name__ == '__main__':
    my_table = HashTable()
    my_table.insert(3)
    my_table.insert(4)
    my_table.insert(128 + 3)
    for i, x in my_table:
        print(f'{i}:, {x}')
    print()
    my_table.delete(3)
    for i, x in my_table:
        print(f'{i}:, {x}')
