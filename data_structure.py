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
        if x == self.NIL:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        self.length -= 1


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
