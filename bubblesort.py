
import numpy as np

def bubblesort(arr):
    n = len(arr)
    cPass = 1
    done = True

    while done:
        done = False
        for i in range(0, n - cPass):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = True
    return arr   


print(bubblesort([99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,76,75,74,73,72,71,79,69,68,67,66,65,63,62,61,59,58,57,56,55,54,53,52,52]))