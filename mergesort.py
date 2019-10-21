import matplotlib
import math
import numpy as np

def mergesort(arr) :
    n = len(arr)
    half = n / 2

    if ( n > 1):

        left = arr[:math.floor(half)]
        right = arr[math.floor(half):]
        mergesort(left)
        mergesort(right)
        merge(arr, left, right)
    return  arr

def merge(arr, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        k = k + 1
        i = i + 1
    while j < len(right):
        arr[k] = right[j]
        k = k + 1
        j = j + 1
    return arr

print(mergesort([5,4,3,2,1]))