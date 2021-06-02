import math
import random
import time
import copy


def mergeSort(lis):
    if len(lis) > 2:
        lis1 = mergeSort(lis[math.floor(len(lis) / 2):])
        lis2 = mergeSort(lis[:math.floor(len(lis) / 2)])
        if len(lis1) > len(lis2):
            lis = mergeTwoLists(lis1, lis2, lis)
        else:
            lis = mergeTwoLists(lis2, lis1, lis)
    else:
        if len(lis) == 1:
            return lis
        if lis[0] > lis[1]:
            temp = lis[0]
            lis[0] = lis[1]
            lis[1] = temp
    return lis


def fillIndex(lis, index, num):
    lis[index] = num
    return lis


def mergeTwoLists(lis1, lis2, lis):
    c = 0
    lisPointer1 = 0
    lisPointer2 = 0
    for position in range(len(lis)):
        if lisPointer1 == len(lis1):
            lis[position] = lis2[lisPointer2]
            lisPointer2 += 1
        elif lisPointer2 == len(lis2):
            lis[position] = lis1[lisPointer1]
            lisPointer1 += 1
        elif lisPointer1 < len(lis1) and lis2[lisPointer2] >= lis1[lisPointer1]:
            lis[position] = lis1[lisPointer1]
            lisPointer1 += 1
        else:
            lis[position] = lis2[lisPointer2]
            lisPointer2 += 1
    return lis


List = [2, 0, 2, 1, 1, 0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortColors(self, head: ListNode):
        c = 0


        mergeSort(head)


if __name__ == "__main__":
    lizard = []
    numTemp = 1000
    for i in range(numTemp):
        lizard.append(random.randrange(0, numTemp))
    print("start")
    lizard2 = copy.copy(lizard)
    start = time.time()
    lizard2 = sorted(lizard2)
    print(f"The Time is: {time.time() - start}")
    # print(lizard)
    print("start")
    start = time.time()
    lizard = mergeSort(lizard)
    print(f"The Time is: {time.time() - start}")
    print(f"{len(lizard)}, {len(lizard2)}")
    for i in range(len(lizard)):
        if lizard[i] != lizard2[i]:
            print(f"NOOOOOO!!!!! ({lizard[i]}, {lizard2[i]})")
            exit()
    if lizard == lizard2:
        print("Hello")
    print(List)
    ret = Solution().sortColors(List)
    print(ret, List)
    # print(lizard)
