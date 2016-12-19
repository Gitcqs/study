#/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a docstring"""
import random
import cProfile
UNSORTEDLIST = []

# generate an unsorted list
def generateunsortedlist(num):
    '''tttttttt'''
    UNSORTEDLIST.clear()
    for i in range(0, num):
        UNSORTEDLIST.append(random.randint(0, 100))
    #print(UNSORTEDLIST)
    print('num :', num)
    print(
        'gene^------^------^------^---------------------------------------------'
    )



#一， 冒泡排序
def bubblesorts(UNSORTEDLIST):
    '''tttttttt'''
    list_length = len(UNSORTEDLIST)
    for i in range(0, list_length - 1):
        for j in range(0, list_length - i - 1):
            if UNSORTEDLIST[j] > UNSORTEDLIST[j + 1]:
                UNSORTEDLIST[j], UNSORTEDLIST[j + 1] = UNSORTEDLIST[
                    j + 1], UNSORTEDLIST[j]
    return UNSORTEDLIST


#一， 冒泡排序
def bubbleSort(UNSORTEDLIST):
    '''tttttttt'''
    list_length = len(UNSORTEDLIST)
    for i in range(0, list_length - 1):
        for j in range(0, list_length - i - 1):
            if UNSORTEDLIST[j] > UNSORTEDLIST[j + 1]:
                UNSORTEDLIST[j], UNSORTEDLIST[j + 1] = UNSORTEDLIST[
                    j + 1], UNSORTEDLIST[j]
    return UNSORTEDLIST


#二，选择排序
def selectionSort(UNSORTEDLIST):
    '''tttttttt'''
    list_length = len(UNSORTEDLIST)
    for i in range(0, list_length - 1):
        for j in range(i + 1, list_length):
            if UNSORTEDLIST[i] > UNSORTEDLIST[j]:
                UNSORTEDLIST[i], UNSORTEDLIST[j] = UNSORTEDLIST[
                    j], UNSORTEDLIST[i]
    return UNSORTEDLIST


#三、插入排序 
def insertionSort(UNSORTEDLIST):
    '''tttttttt'''
    list_length = len(UNSORTEDLIST)
    if list_length < 2:
        return UNSORTEDLIST
    for i in range(1, list_length):
        key = UNSORTEDLIST[i]
        j = i - 1
        while j >= 0 and key < UNSORTEDLIST[j]:
            UNSORTEDLIST[j + 1] = UNSORTEDLIST[j]
            j = j - 1
        UNSORTEDLIST[j + 1] = key
    return UNSORTEDLIST


#四，归并排序
def mergeSort(UNSORTEDLIST):
    '''tttttttt'''
    if len(UNSORTEDLIST) < 2:
        return UNSORTEDLIST
    sortedList = []
    left = mergeSort(UNSORTEDLIST[:int(len(UNSORTEDLIST) / 2)])
    right = mergeSort(UNSORTEDLIST[int(len(UNSORTEDLIST) / 2):])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sortedList.append(left.pop(0))
        else:
            sortedList.append(right.pop(0))
    if len(left) > 0:
        sortedList.extend(mergeSort(left))
    else:
        sortedList.extend(mergeSort(right))
    return sortedList


#五，快速排序
def quickSort(UNSORTEDLIST):
    '''tttttttt'''
    if len(UNSORTEDLIST) < 2:
        return UNSORTEDLIST
    less = []
    greater = []
    middle = UNSORTEDLIST.pop(0)
    for item in UNSORTEDLIST:
        if item < middle:
            less.append(item)
        else:
            greater.append(item)
    return quickSort(less) + [middle] + quickSort(greater)


#六，堆排序
def maxHeapify(L, heap_size, i):
    '''tttttttt'''
    leftChildIndex = 2 * i + 1
    rightChildIndex = 2 * i + 2
    # print 'leftChildIndex=',leftChildIndex
    # print 'rightChildIndex=',rightChildIndex
    largest = i
    if leftChildIndex < heap_size and L[int(leftChildIndex)] > L[int(largest)]:
        largest = leftChildIndex
    if rightChildIndex < heap_size and L[int(rightChildIndex)] > L[int(
            largest)]:
        largest = rightChildIndex
    if largest != i:
        L[int(i)], L[int(largest)] = L[int(largest)], L[int(i)]
        maxHeapify(L, heap_size, largest)


def buildMaxHeap(L):
    heap_size = len(L)
    if heap_size > 1:
        start = heap_size / 2 - 1
        # print 'start=',start
    while start >= 0:
        maxHeapify(L, heap_size, start)
        start = start - 1


def heapSort(L):
    heap_size = len(L)
    buildMaxHeap(L)
    i = heap_size - 1
    while i > 0:
        L[0], L[i] = L[i], L[0]
        heap_size = heap_size - 1
        i = i - 1
        maxHeapify(L, heap_size, 0)
    return L


if __name__ == '__main__':
    generateunsortedlist(2000)
    #print(UNSORTEDLIST)
    print('~~~~~~~~~~~~~~~~~~~~冒泡排序性能~~~~~~~~~~~~~~~~~~~~')
    cProfile.run('bubbleSort(UNSORTEDLIST)')
    generateunsortedlist(2000)
    print('~~~~~~~~~~~~~~~~~~~~选择排序性能~~~~~~~~~~~~~~~~~~~~')
    cProfile.run('selectionSort(UNSORTEDLIST)')
    generateunsortedlist(2000)
    print('~~~~~~~~~~~~~~~~~~~~插入排序性能~~~~~~~~~~~~~~~~~~~~')
    cProfile.run('insertionSort(UNSORTEDLIST)')
    generateunsortedlist(2000)
    print('~~~~~~~~~~~~~~~~~~~~归并排序性能~~~~~~~~~~~~~~~~~~~~')
    cProfile.run('mergeSort(UNSORTEDLIST)')
    generateunsortedlist(2000)
    print('~~~~~~~~~~~~~~~~~~~~快速排序性能~~~~~~~~~~~~~~~~~~~~')
    cProfile.run('quickSort(UNSORTEDLIST)')
    generateunsortedlist(2000)
    print('~~~~~~~~~~~~~~~~~~~~堆排序性能~~~~~~~~~~~~~~~~~~~~')
    cProfile.run('heapSort(UNSORTEDLIST)')
