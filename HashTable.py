
import random, math

class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SortedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, x):
        new_node = ListNode(x)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return
            
        node = self.head
        prev = None
        while node and node.value < x:
            prev = node
            node = node.next

        if node == self.head:
            self.head = new_node
        else:
            prev.next = new_node
        
        new_node.next = node

        self.size += 1

    def pop(self):
        if self.head is None:
            return None

        x = self.head.value
        self.head = self.head.next
        self.size =- 1

        return x

    def delete(self, x):
        node = self.head
        prev = None
        while node and node.value != x:
            prev = node
            node = node.next

        if not node:
            return

        if node == self.head:
            self.head = node.next
        else:
            prev.next = node.next

        self.size -= 1

        return node.value

    def __str__(self):
        node = self.head
        string = ''
        while node:
            string += str(node.value) + ' ' 
            node = node.next
        string.strip()
        return string


class HashTable:
    '''Set with repetitions (bag)'''
    def __init__(self):
        self.m = 128
        self.a = random.randint(0, 2**64 - 1)
        self._table = [SortedList() for _ in range(self.m)]
        self._iter_idx = None

    def insert(self, x):
        idx = self._hash(x)
        self._table[idx].insert(x)

    def delete(self, x):
        idx = self._hash(x)
        self._table[idx].delete(x)

    def _hash(self, k):
        w = 64
        l = int(math.log2(self.m))
        h = (k*self.a % 2**w) >> (w-l)
        return h

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):
        if self._iter_idx is None or self._iter_idx == len(self._table):
            raise StopIteration

        while self._table[self._iter_idx].head is None:
            self._iter_idx += 1
            if self._iter_idx == len(self._table):
                raise StopIteration

        self._iter_idx += 1
        return self._table[self._iter_idx-1]


#######################################################

if __name__ == '__main__':
    # my_list = SortedList()
    # my_list.insert(2)
    # my_list.insert(3)
    # my_list.insert(1)
    # my_list.insert(6)
    # my_list.insert(5)
    # print(my_list)
    # print(my_list.pop())
    # print(my_list.delete(5))
    # print(my_list)

    my_table = HashTable()
    my_table.insert(1)
    my_table.insert(4)
    my_table.insert(2)
    my_table.insert(4)
    my_table.insert(3)
    for x in my_table:
        print(x)
    print()
    my_table.delete(2)
    my_table.delete(4)
    for x in my_table:
        print(x)
