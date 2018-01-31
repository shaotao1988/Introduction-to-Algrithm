#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class HeapSort(object):
    def __init__(self, data):
        self.data = data[:]
        self.length = len(data)
        self.heap_size = len(data)

    def left(self, index):
        return 2*index

    def right(self, index):
        return 2*index+1

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
        # The index bigger than self.length/2 are leaves, ie. max heap with size 1
        for i in range(self.length//2, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.make_max_heap()
        for i in range(self.heap_size-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heap_size -= 1
            self.max_heapify(0)


class AlSort(object):
    def __init__(self, data):
        self.data = data[:]

    def InsertionSort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i-1
            while j>=0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j = j-1
            self.data[j+1] = key            

    def MergeSort(self, p, r):
        if p < r:
            q = (p+r)//2
            self.MergeSort(p, q)
            self.MergeSort(q+1, r)
            self.Merge(p, q, r)

    def Merge(self, p, q, r):
        left = self.data[p:q+1]
        left.append(sys.maxsize)
        right = self.data[q+1: r+1]
        right.append(sys.maxsize)
        i = 0
        j = 0
        count = 0
        while count < r-p+1:
            if left[i] < right[j]:
                self.data[p+count] = left[i]
                i += 1
                count += 1
            else:
                self.data[p+count] = right[j]
                j += 1
                count += 1


if __name__ == "__main__":
    testdata = [2, 3, 25, 12, 5, 6, 67, 43, 9]
    result = [2, 3, 5, 6, 9, 12, 25, 43, 67]
    Sort = AlSort(testdata)
    Sort.InsertionSort()
    if Sort.data != result:
        print("test InsertionSort wrong:", Sort.data)
    print(Sort.data)
    Sort = AlSort(testdata)
    Sort.MergeSort(0, len(testdata)-1)
    if Sort.data != result:
        print("test MergeSort wrong:", Sort.data)
    print(Sort.data)
    HR = HeapSort(testdata)
    HR.heap_sort()
    if HR.data != result:
        print("test HeapSort wrong:", HR.data)
    print(HR.data)


