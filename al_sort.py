#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from al_heap import Heap

class QuickSort(object):
    def __init__(self, data):
        self.data = data[:]

    def partition(self, start, end):
        x = self.data[end]
        i = start
        j = start
        for j in range(start, end):
            if self.data[j] < x:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1
            j += 1
        self.data[i], self.data[end] = self.data[end], self.data[i]
        return i

    def quick_sort(self, start, end):
        if start < end:
            p = self.partition(start, end)
            self.quick_sort(start, p-1)
            self.quick_sort(p+1, end)

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


class HeapSort(Heap):
    def __init__(self, data):
        Heap.__init__(self, data)

    def heap_sort(self):
        self.make_max_heap()
        for i in range(self.heap_size-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heap_size -= 1
            self.max_heapify(0)

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
    QS = QuickSort(testdata)
    QS.quick_sort(0, len(testdata)-1)
    if HR.data != result:
        print("test QuickSort wrong:", QS.data)
    print(QS.data)


