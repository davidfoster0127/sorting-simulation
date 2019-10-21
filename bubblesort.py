from matplotlib import pyplot
import numpy 
import timeit
import random

from functools import partial
def bubblesort(arr):
    n = len(arr)
    cPass = 1
    done = True

    while done:
        done = False
        for i in range(0, n - cPass):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                done = True
    return arr

def bubblesort2(arr):
    memory = 0

    n = len(cp)
    memory += n

    done = True
    memory += 1

    temp = ''
    memory += 1

    while done:
        done = False
        for i in range(0, n - 1):
            if cp[i] > cp[i + 1]:
                temp = cp[i + 1]
                cp[i + 1] = cp[i]
                cp[i] = temp
                done = True

    return cp, memory


# print(bubblesort([5,4,3,2,1]))