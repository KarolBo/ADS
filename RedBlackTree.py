from collections import deque

class Node:
    def __init__(self, x):
        self.val = x
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'

class RedBlackTree:
    def __init__(self):
        self.setinel = Node(None)
        self.setinel.left = self.setinel
        self.setinel.right = self.setinel
        self.head = self.setinel
        self.setinel.color = 'black'

    def insert(self, x):
        parent = self.search(x)
        new_node = Node(x)
        if not parent:
            self.head = new_node
            self.head.color = 'black'
        elif x < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.left = self.setinel
        new_node.right = self.setinel
        new_node.parent = parent
        
        self.fixup(new_node)

    def search(self, x):
        node = self.head
        parent = None
        while node.val:
            parent = node
            if x < node.val:
                node = node.left
            else:
                node = node.right
        return parent

    def fixup(self, new_node):
        while new_node.parent and new_node.parent.color == 'red':
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.color == 'red':
                    new_node = new_node.parent.parent
                    self.recolor(new_node)
                    continue
                if new_node == new_node.parent.right: # zig-zag
                    new_node = new_node.parent
                    self.left_rotate(new_node)
                self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.color == 'red':
                    new_node = new_node.parent.parent
                    self.recolor(new_node)
                    continue
                if new_node == new_node.parent.left: # zig-zag
                    new_node = new_node.parent
                    self.right_rotate(new_node)
                self.left_rotate(new_node.parent.parent)
        self.head.color = 'black'

    def recolor(self, node):
        print('recolor')
        if node != self.head:
            node.color = 'red'
        node.left.color = 'black'
        node.right.color = 'black'

    def left_rotate(self, x):
        print('rotate left')
        y = x.right
        # parent - y
        y.parent = x.parent
        if x == self.head:
            self.head = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        # y.left - x.right
        x.right = y.left
        y.left.parent = x
        # y - x
        y.left = x
        x.parent = y
        # recolor
        y.color = 'black'
        x.color = 'red'
        if y.right != self.setinel:
            y.right.color = 'red'

    def right_rotate(self, x):
        print('rotate right')
        y = x.left
        # parent - y
        y.parent = x.parent
        if x == self.head:
            self.head = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        # y.left - x.right
        x.left = y.right
        y.right.parent = x
        # y - x
        y.right = x
        x.parent = y
        # recolor
        y.color = 'black'
        x.color = 'red'
        if y.left != self.setinel:
            y.left.color = 'red'
  
    def inorder(self, node='start'):
        if node == 'start':
            node = self.head
        if not node.val:
            return
        self.inorder(node.left)
        print(node.val, ' ', end='')
        self.inorder(node.right)

    def level_order(self):
        queue = deque()
        queue.append((self.head, 0))
        cur_depth = 0
        while len(queue):
            node, new_depth = queue.popleft()
            if new_depth > cur_depth:
                print()
                cur_depth = new_depth
            if not node.val:
                print('NIL', end=', ')
                continue
            print(node.val, node.color[0], end=', ')
            queue.append((node.left, cur_depth + 1))
            queue.append((node.right, cur_depth + 1))
        print()
        

#########################################

my_tree = RedBlackTree()
my_tree.insert(10)
my_tree.insert(20)
my_tree.insert(30)
my_tree.insert(50)
my_tree.insert(40)
my_tree.insert(60)
my_tree.insert(70)
my_tree.insert(80)
my_tree.insert(4)
my_tree.insert(8)
# my_tree.inorder()
my_tree.level_order()