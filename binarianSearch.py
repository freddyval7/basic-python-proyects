import random
import time

def naiveSearch(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1 

def binarianSearch(list, target, low = None, sup = None):
    # The list must be sorted in ascending order
    sorted(list)

    if low is None:
        low = 0 # Start
    if sup is None:
        sup = len(list)-1 # Final

    if sup < low:
        return -1

    middlePoint = (low + sup) // 2

    if list[middlePoint] == target:
        return middlePoint
    elif target < list[middlePoint]:
        return binarianSearch(list, target, low, middlePoint-1)
    else:
        return binarianSearch(list, target, middlePoint+1, sup)
