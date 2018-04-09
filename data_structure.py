#!/usr/bin/python
# -*- coding = utf-8 -*-


class ListNode(object):
    def __init__(self, key = 0):
        self.key = key
        self.prev = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.NIL = ListNode()
        self.NIL.prev = self.NIL
        self.NIL.next = self.NIL
        self.length = 0

    def insert(self, x):
        x.next = self.NIL.next
        x.next.prev = x
        self.NIL.next = x
        x.prev = self.NIL
        self.length += 1

    def find(self, key):
        x = self.NIL.next
        while x != self.NIL and x.key != key:
            x = x.next
        return x

    def delete(self, x):
        if not isinstance(x, ListNode):
            x = self.find(x)
        if x == self.NIL:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        self.length -= 1

class Heap(object):
    def __init__(self, data, cmp = None):
        self.data = data
        self.heap_size = len(data)
        self.cmp = cmp

    def left(self, index):
        return 2*index

    def right(self, index):
        return 2*index+1

    def parent(self, index):
        return index//2

    def has(self, data):
        index = 0
        try:
            index = self.data.index(data)
        except:
            return False
        else:
            if index >= self.heap_size or index < 0:
                return False
            return True

    """
    Suggest both children rooted at left(index) and right(index) are max heap
    But data[index] might be smaller than it's children
    max_heapify maintains the binary tree rooted at index to be max heap
    """
    def max_heapify(self, index):
        l = self.left(index)
        r = self.right(index)
        largest = index
        if l < self.heap_size and self.compare(self.data[l], self.data[largest]) > 0:
            largest = l
        if r < self.heap_size and self.compare(self.data[r], self.data[largest]) > 0:
            largest = r
        # If child is largest, exchange with largest child and continue maintain max heap rooted at child
        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self.max_heapify(largest)

    def make_max_heap(self):
        # The index bigger than self.heap_size/2 are leaves, ie. max heap with size 1
        for i in range(self.heap_size//2, -1, -1):
            self.max_heapify(i)

    def compare(self, u, v):
        if self.cmp == None:
            if u>v:
                return 1
            elif u<v:
                return 0
            else:
                return -1
        else:
            return self.cmp(u, v)

    def min_heapify(self, index):
        l = self.left(index)
        r = self.right(index)
        minimal = index
        if l < self.heap_size and self.compare(self.data[l], self.data[minimal]) < 0:
            minimal = l
        if r < self.heap_size and self.compare(self.data[r], self.data[minimal]) < 0:
            minimal = r
        # If child is largest, exchange with largest child and continue maintain max heap rooted at child
        if minimal != index:
            self.data[index], self.data[minimal] = self.data[minimal], self.data[index]
            self.max_heapify(minimal)

    def make_min_heap(self):
        # The index bigger than self.heap_size/2 are leaves, ie. max heap with size 1
        for i in range(self.heap_size//2, -1, -1):
            self.min_heapify(i)


class MinPriorityQueue(Heap):
    def __init__(self, data, cmp):
        Heap.__init__(self, data, cmp)
        self.make_min_heap()

    def minimal(self):
        return self.data[0]

    def insert(self, x):
        self.data.append(x)
        self.heap_size += 1
        index = self.heap_size-1
        while index > 0 and self.compare(self.data[self.parent(index)], self.data[index]) > 0:
            self.data[self.parent(index)], self.data[index] = self.data[index], self.data[self.parent(index)]
            index = self.parent(index)

    def extract_min(self):
        if self.heap_size == 0:
            return None
        v = self.data[0]
        self.data[0], self.data[self.heap_size-1] = self.data[self.heap_size-1], self.data[0]
        self.heap_size -= 1
        self.min_heapify(0)
        return v

    def find_index(self, x):
        return self.data.index(x)

    def decrease_key(self, x, weight):
        index = self.data.index(x)
        if index == -1:
            print("key is not in queue")
            return -1
        if self.data[index].weight < weight:
            print("The decreased value is more than original value")
            return -1
        self.data[index].weight = weight
        while index > 0 and self.compare(self.data[self.parent(index)], self.data[index]) > 0:
            self.data[self.parent(index)], self.data[index] = self.data[index], self.data[self.parent(index)]
            index = self.parent(index)
        return index


class MaxPriorityQueue(Heap):
    def __init__(self, data):
        Heap.__init__(self, data)
        self.make_max_heap()

    def maximum(self):
        return self.data[0]

    def insert(self, x):
        self.data.append(x)
        self.heap_size += 1
        index = self.heap_size-1
        while index > 0 and self.compare(self.data[self.parent(index)], self.data[index]) < 0:
            self.data[self.parent(index)], self.data[index] = self.data[index], self.data[self.parent(index)]
            index = self.parent(index)

    def extract_max(self):
        if self.heap_size == 0:
            return None
        v = self.data[0]
        self.data[0] = self.data[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)
        return v

    def increase_key(self, index, x):
        if self.data[index] > x:
            print("The increased value is less than original value")
            return -1
        self.data[index] = x
        while index > 0 and self.compare(self.data[self.parent(index)], self.data[index]) < 0:
            self.data[self.parent(index)], self.data[index] = self.data[index], self.data[self.parent(index)]
            index = self.parent(index)
        return index


class BinaryTreeNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


class BinaryTree(object):
    def __init__(self):
        self.root = None
    @staticmethod
    def inoder_tree_walk(x):
        if x == None:
            return
        BinaryTree.inoder_tree_walk(x.left)
        print(x.value)
        BinaryTree.inoder_tree_walk(x.right)


class BinarySearchTree(BinaryTree):
    @staticmethod
    def maximum(x):
        cur = x
        while cur != None and cur.right != None:
            cur = cur.right
        return cur

    @staticmethod
    def minimum(x):
        cur = x
        while cur != None and cur.left != None:
            cur = cur.left
        return cur

    def search(self, key):
        cur = self.root
        while cur != None and cur.value != key:
            if key < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return cur

    def successor(self, x):
        if x.right != None:
            return self.minimum(x.right)
        # 找到第一个左子树祖先
        while x.p != None and x.p.right == x:
            x = x.p
        return x.p

    def predecessor(self, x):
        if x.left != None:
            return self.maximum(x.left)
        # 找到第一个右子树祖先
        while x.p != None and x.p.left == x:
            x = x.p
        return x.p

    def insert(self, x):
        if self.root == None:
            self.root = x
            return
        cur = self.root
        y = None
        while cur != None:
            y = cur
            if x.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        if x.value < y.value:
            y.left = x
        else:
            y.right = x
        x.parent = y
        return

    # 节点移植，只处理old和new节点的北向连接
    def transplant(self, old, new):
        if old == self.root:
            self.root = new
            return
        if old.parent.left == old:
            old.parent.left = new
        else:
            old.parent.right = new
        if new != None:
            new.parent = old.parent

    def delete(self, x):
        # 如果x只存在一个子树，则以该子树替换x
        if x.left == None:
            self.transplant(x, x.right)
        elif x.right == None:
            self.transplant(x, x.left)
        else:
            # x的左右子树均存在，则将x替换为x的后继(也可以替换为前驱)
            y = self.minimum(x.right)
            # y一定是x的右子树中：最左下方的节点；或者根节点(x的右子树没有左孩子)
            if y.parent != x:
                self.transplant(y, y.right)
                y.right = x.right
                y.right.parent = y
                y.left = x.left
                y.left.parent = y
                self.transplant(x, y)
            else:
                y.left = x.left
                y.left.parent = y
                self.transplant(x, y)
        x.parent = None
        x.right = None
        x.left = None


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(ListNode(1))
    linked_list.insert(ListNode(2))
    linked_list.insert(ListNode(3))
    if linked_list.length != 3:
        print('length test fail, length = ', linked_list.length, ", should be: 3")
    x = linked_list.find(2)
    if x == linked_list.NIL:
        print('find test fail')
    linked_list.delete(x)
    x = linked_list.find(1)
    if x == linked_list.NIL:
        print('delete test fail')
    x = linked_list.find(4)
    if x != linked_list.NIL:
        print('find test fail')

    T = BinarySearchTree()
    testdata = [2, 3, 25, 12, 5, 6, 67, 43, 9]
    for i in range(0, len(testdata)):
        node = BinaryTreeNode(testdata[i])
        T.insert(node)
    T.inoder_tree_walk(T.root)
    x = T.search(6)
    if x == None or x.value != 6:
        print('search test failed')
    T.delete(x)
    T.inoder_tree_walk(T.root)
    T.insert(x)
    T.inoder_tree_walk(T.root)




