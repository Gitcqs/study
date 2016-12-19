#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

unsortedList=[]

# generate an unsorted list
def generateUnsortedList(num):
	for i in range(0,num):
		unsortedList.append(random.randint(0,100))
	print unsortedList

# 冒泡排序
def bubbleSort(unsortedList):
	list_length=len(unsortedList)
	for i in range(0,list_length-1):
		for j in range(0,list_length-i-1):
			if unsortedList[j]>unsortedList[j+1]:
				unsortedList[j],unsortedList[j+1]=unsortedList[j+1],unsortedList[j]
	return unsortedList

generateUnsortedList(20)
print bubbleSort(unsortedList)


# 选择排序
def selectionSort(unsortedList):
	list_length=len(unsortedList)
	for i in range(0,list_length-1):
		for j in range(i+1,list_length):
			if unsortedList[i]>unsortedList[j]:
				unsortedList[i],unsortedList[j]=unsortedList[j],unsortedList[i]
	return unsortedList

	
#三、插入排序	
def insertionSort(unsortedList):
	list_length=len(unsortedList)
	if list_length<2:
		return unsortedList
	for i in range(1,list_length):
		key=unsortedList[i]
		j=i-1
		while j>=0 and key<unsortedList[j]:
			unsortedList[j+1]=unsortedList[j]
			j=j-1
		unsortedList[j+1]=key
	return unsortedList

# 归并排序
def mergeSort(unsortedList):
	if len(unsortedList)<2:
		return unsortedList
	sortedList=[]
	left=mergeSort(unsortedList[:len(unsortedList)/2])
	right=mergeSort(unsortedList[len(unsortedList)/2:])
	while len(left)>0 and len(right)>0:
		if left[0]<right[0]:
			sortedList.append(left.pop(0))
		else:
			sortedList.append(right.pop(0))
	if len(left)>0:
		sortedList.extend(mergeSort(left))
	else:
		sortedList.extend(mergeSort(right))
	return sortedList


#快速排序
def quickSort(unsortedList):
	if len(unsortedList)<2:
		return unsortedList
	less=[]
	greater=[]
	middle=unsortedList.pop(0)
	for item in unsortedList:
		if item<middle:
			less.append(item)
		else:
			greater.append(item)
	return quickSort(less)+[middle]+quickSort(greater)

#六，堆排序
def maxHeapify(L,heap_size,i):
    leftChildIndex=2*i+1
    rightChildIndex=2*i+2
    # print 'leftChildIndex=',leftChildIndex
    # print 'rightChildIndex=',rightChildIndex
    largest=i
    if leftChildIndex<heap_size and L[leftChildIndex]>L[largest]:
        largest=leftChildIndex
    if rightChildIndex<heap_size and L[rightChildIndex]>L[largest]:
        largest=rightChildIndex
    if largest!=i:
        L[i],L[largest]=L[largest],L[i]
        maxHeapify(L,heap_size,largest)

def buildMaxHeap(L):
    heap_size=len(L)
    if heap_size>1:
        start=heap_size/2-1
        # print 'start=',start
    while start>=0:
        maxHeapify(L,heap_size,start)
        start=start-1

def heapSort(L):
    heap_size=len(L)
    buildMaxHeap(L)
    i=heap_size-1
    while i>0:
        L[0],L[i]=L[i],L[0]
        heap_size=heap_size-1
        i=i-1
        maxHeapify(L,heap_size,0)
    return L









