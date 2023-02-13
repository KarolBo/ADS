class SegmentTree:
    def __init__(self, arr, semigroup=None):
        if semigroup:
            self.operation, self.neutral = semigroup
        else:
            self.operation = lambda a, b: a + b
            self.neutral = 0

        self.n = len(arr)
        self._arr = (4*self.n) * [0]
        for i, val in enumerate(arr):
            self.update(i, val)

    def update(self, arrIdx, val):
        def update_iter(left, right, treeIdx):
            if left == right:
                self._arr[treeIdx] = val
                return

            m = (left + right) // 2
            left_child = 2 * treeIdx + 1
            right_child = 2 * treeIdx + 2
            if arrIdx <= m:
                update_iter(left, m, left_child)
            else:
                update_iter(m+1, right, right_child)

            self._arr[treeIdx] = self.operation(self._arr[left_child], self._arr[right_child])
        update_iter(0, self.n - 1, 0)

    def query(self, a, b):
        def query_iter(left, right, treeIdx):
            if right < a or left > b:
                return self.neutral

            if left >= a and right <= b:
                return self._arr[treeIdx]

            m = (left + right) // 2
            left_child = 2 * treeIdx + 1
            right_child = 2 * treeIdx + 2
            return self.operation(
                query_iter(left, m, left_child),
                query_iter(m+1, right, right_child)
            )
        return query_iter(0, self.n-1, 0)


class BinaryIndexedTree:
    def __init__(self, arr):
        self._n = len(arr) + 1
        self._arr = self._n * [0]
        for i, val in enumerate(arr):
            self.update(i, val)

    def update(self, i, val):
        i += 1
        while i <= self._n:
            self._arr[i] += val
            i += i & (-i)

    def query(self, i):
        i += 1
        acc = 0
        while i > 0:
            acc += self._arr[i]
            i -= i & (-i)
        return acc

############################################################################################

arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
tree = SegmentTree(arr)
print('Segment tree:')
print(tree.query(2, 8)) # 123
print()
bit = BinaryIndexedTree(arr)
print('Fenwick tree:')
print(bit.query(8) - bit.query(1))
