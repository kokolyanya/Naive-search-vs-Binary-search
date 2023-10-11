#we want to prove that binary search is faster than naive search
#naive search: scan entire list and ask if its equals to the target
#binary search: scan at the half of the list and ask if its equals to the target,
#or smaller or bigger, and continue in the half of the list where the target is
#we need to sort the list for the binary search

import random
import time

def naiveSearch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binarySearch(l, target, low = None, high = None):
    if low == None:
        low = 0
    if high == None:
        high = len(l)-1
    
    if high < low:
        return -1
    
    midpoint = (low+high)//2
    if target ==  l[midpoint]:
        return midpoint
    elif target < l[midpoint]:
        return binarySearch(l, target, low, midpoint-1)
    else:
        return binarySearch(l, target, midpoint+1, high)

if __name__=='__main__':
    # l = [1,3,5,10,12]
    # target = 10
    # print(naiveSearch(l, target))
    # print(binarySearch(l, target))

    length = 10000
    sortedList = set()
    while len(sortedList) < length:
        sortedList.add(random.randint(-3*length, 3*length))
    sortedList = sorted(list(sortedList))

    start = time.time()
    for target in sortedList:
        naiveSearch(sortedList, target)
    end = time.time()
    print("Naive search time : ",(end-start)/length, "seconds")

    start = time.time()
    for target in sortedList:
        binarySearch(sortedList, target)
    end = time.time()
    print("Binary search time : ",(end-start)/length, "seconds")
    

