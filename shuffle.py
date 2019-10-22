import numpy as np
import random
from math import floor

def randomize():
    arr =  np.arange(100)
    length = len(arr)
    y = floor(length * .9)
    random.shuffle(arr[0:y-1])
    return arr

print(randomize())

# Will replace with the algorithm that uses mergesort if necessary
def getInvCount(arr): 
    n = len(arr)
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 
  
print("Number of inversions are", 
getInvCount(randomize())) 