#!/usr/python/bin
# -*- coding = utf-8 -*-


class Heap(object):
    def __init__(self, data):
        self.data = data[:]
        self.heap_size = len(data)

    def left(self, index):
        return 2*index

    def right(self, index):
        return 2*index+1

    def parent(self, index):
        return index//2

    """
    Suggest both children rooted at left(index) and right(index) are max heap
    But data[index] might be smaller than it's children
    max_heapify maintains the binary tree rooted at index to be max heap
    """
    def max_heapify(self, index):
        l = self.left(index)
        r = self.right(index)
        largest = index
        if l < self.heap_size and self.data[l] > self.data[largest]:
            largest = l
        if r < self.heap_size and self.data[r] > self.data[largest]:
            largest = r
        # If child is largest, exchange with largest child and continue maintain max heap rooted at child
        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self.max_heapify(largest)

    def make_max_heap(self):
        # The index bigger than self.heap_size/2 are leaves, ie. max heap with size 1
        for i in range(self.heap_size//2, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.make_max_heap()


class HeapSort(Heap):
    def __init__(self, data):
        Heap.__init__(self, data)

    def heap_sort(self):
        self.make_max_heap()
        for i in range(self.heap_size-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heap_size -= 1
            self.max_heapify(0)

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
        while index > 0 and self.data[self.parent(index)] < self.data[index]:
            self.data[self.parent(index)], self.data[index] = self.data[index], self.data[self.parent(index)]
            index = self.parent(index)

    def extract_max(self):
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
        while index > 0 and self.data[self.parent(index)] < self.data[index]:
            self.data[self.parent(index)], self.data[index] = self.data[index], self.data[self.parent(index)]
            index = self.parent(index)
        return index


if __name__ == "__main__":
    testdata = [2, 3, 25, 12, 5, 6, 67, 43, 9]
    
    result = [2, 3, 5, 6, 9, 12, 25, 43, 67]
    HR = HeapSort(testdata)
    HR.heap_sort()
    if HR.data != result:
        print("test HeapSort wrong:", HR.data)
    print(HR.data)

    PQ = MaxPriorityQueue(testdata)
    if PQ.maximum() != max(testdata):
        print("maximum test fail", PQ.maximum(), max(testdata))
    PQ.insert(100)
    if PQ.maximum() != 100:
        print("insert test fail")
    PQ.increase_key(3, 195)
    if PQ.maximum() != 195:
        print("increase_key test fail") 
    if PQ.extract_max() != 195:
        print("extract_max test fail")
    if PQ.extract_max() != 100:
        print("extract_max test fail")


