class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, arr=None):
        self.size = 0
        self.head = None
        
        if not arr:
            return 

        for a in arr:
            self.insert(a, self.size)

    def __str__(self):
        string = ''
        node = self.head
        while node is not None:
            string += str(node.value) + ' '
            node = node.next
        return string

    def insert(self, x, idx):
        if idx > self.size:
            return

        new_node = Node(x)
        node = self.head
        prev = None
        i = 0

        while i < idx:
            prev = node
            node = node.next
            i += 1

        new_node.next = node

        if prev:
            prev.next = new_node
        else:
            self.head = new_node

        self.size += 1

    def pop(self, idx):
        if idx > self.size:
            return

        node = self.head
        prev = None
        i = 0
        while i < idx:
            prev = node
            node = node.next
            i += 1

        prev.next = node.next

        if node == self.head:
            self.head = node.next

        return node.value

    def find(self, x):
        node = self.head
        while node:
            if node.value == x:
                return True
            node = node.next
        return False

    def revert(self, l, r):
        prev = None
        node = self.head
        i = 0
        while i <= l:
            last_out = prev
            prev = node
            node = node.next
            i += 1

        first_in = prev

        while i <= r:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            i += 1

        first_in.next = node
        if l == 0:
            self.head = prev
        else:
            last_out.next = prev

    def sort(self, list):
        if list.size == 1:
            return list
        list1, list2 = self._split(list)
        list1 = self.sort(list1)
        list2 = self.sort(list2)
        return self._merge(list1, list2)
        
    @staticmethod
    def _split(list):
        m = list.size // 2
        list1 = LinkedList()
        list2 = LinkedList()
        node = list.head
        i = 0
        while i < m:
            list1.insert(node.value, list1.size)
            node = node.next
            i += 1
        while i < list.size:
            list2.insert(node.value, list2.size)
            node = node.next
            i += 1
        return list1, list2

    @staticmethod
    def _merge(list1, list2):
        node1 = list1.head
        node2 = list2.head
        merged = LinkedList()

        while node1 and node2:
            if node1.value < node2.value:
                merged.insert(node1.value, merged.size)
                node1 = node1.next
            else:
                merged.insert(node2.value, merged.size) 
                node2 = node2.next
        while node1:
            merged.insert(node1.value, merged.size)
            node1 = node1.next
        while node2:
            merged.insert(node2.value, merged.size)
            node2 = node2.next
        return merged

################################################

my_list = LinkedList([3, 4, 5, 2, 3, 9, 1])
print(my_list)
print(my_list.sort(my_list))

# print()
# print(list.pop(1))
# print()
# list.print()
# print(list.find(5))
# print(list.find(10))