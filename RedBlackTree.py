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
        self.root = self.setinel
        self.setinel.color = 'black'

    def insert(self, x):
        parent = self.searchParent(x)
        new_node = Node(x)
        if not parent:
            self.root = new_node
            self.root.color = 'black'
        elif x < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.left = self.setinel
        new_node.right = self.setinel
        new_node.parent = parent
        
        self.insert_fixup(new_node)

    def searchParent(self, x):
        node = self.root
        parent = None
        while node.val:
            parent = node
            if x < node.val:
                node = node.left
            else:
                node = node.right
        return parent

    def insert_fixup(self, new_node):
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
        self.root.color = 'black'

    def recolor(self, node):
        # print('recolor')
        if node != self.root:
            node.color = 'red'
        node.left.color = 'black'
        node.right.color = 'black'

    def left_rotate(self, x):
        # print('rotate left')
        y = x.right
        # parent - y
        y.parent = x.parent
        if x == self.root:
            self.root = y
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
        # print('rotate right')
        y = x.left
        # parent - y
        y.parent = x.parent
        if x == self.root:
            self.root = y
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
            node = self.root
        if not node.val:
            return
        self.inorder(node.left)
        print(node.val, ' ', end='')
        self.inorder(node.right)

    def level_order(self):
        # h = self.get_height()
        # leaves = 2**h
        queue = deque()
        queue.append((self.root, 0))
        cur_depth = 0
        while len(queue):
            node, new_depth = queue.popleft()
            if new_depth > cur_depth:
                print()
                cur_depth = new_depth
            if not node.val:
                print('NIL', end=' ')
                continue
            print(str(node.val)+node.color[0], end=' ')
            queue.append((node.left, cur_depth + 1))
            queue.append((node.right, cur_depth + 1))
        print()
        
    def get_height(self):
        max_h = 0
        q = deque()
        q.append((self.root, 1))
        while len(q):
            node, h = q.popleft()
            if not node.val:
                continue
            max_h = max(max_h, h)
            q.append((node.left, h+1)) 
            q.append((node.right, h+1)) 
        return max_h

    def delete(self, x):
        violation = False
        to_del = self.search(x)
        if not to_del:
            print('Value', x, 'not found')
            return 
        if to_del.left.val is None:
            self.transplant(to_del, to_del.right)
            to_del.right.color = 'black'
            if to_del.color == 'black':
                self.delete_fixup(to_del.right)
        elif to_del.right.val is None:
            self.transplant(to_del, to_del.left)
            to_del.left.color = 'black'
            if to_del.color == 'black':
                self.delete_fixup(to_del.left)
        else:
            pred = self.predecessor(to_del)
            self.delete(pred.val)
            to_del.val = pred.val
        if violation:
            self.delete_fixup(to_del)
                  
    def search(self, x):
        node = self.root
        while node.val:
            if x == node.val:
                return node
            if x < node.val:
                node = node.left
            else:
                node = node.right

    def predecessor(self, node):
        if not node.left.val:
            return None
        node = node.left
        while node.right.val:
            node = node.right
        return node

    def transplant(self, x, y):
        if x == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent

    def delete_fixup(self, node):
        while node.color == 'black' and node != self.root:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    node.parent.color, sibling.color = sibling.color, node.parent.color
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right.color == 'black': # zig-zag
                        sibling.color = 'red'
                        sibling.left.color = 'black'
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    node.parent.color, sibling.color = sibling.color, node.parent.color
                    sibling.right.color = 'black'
                    self.left_rotate(node.parent)
                    break
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    node.parent.color, sibling.color = sibling.color, node.parent.color
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black': # zig-zag
                        sibling.color = 'red'
                        sibling.right.color = 'black'
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    node.parent.color, sibling.color = sibling.color, node.parent.color
                    sibling.left.color = 'black'
                    self.right_rotate(node.parent)
                    break
        node.color = 'black'

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
my_tree.delete(40)
# my_tree.delete(8)
my_tree.level_order()
# print(my_tree.get_height())