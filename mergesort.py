import matplotlib
import math

def mergesort(arr) :
    n = len(arr)
    half = math.floor(n / 2);
    if ( n > 0):
        left = arr.copy()
        right = arr.copy()
        print(left)
        print(right)
    return len(arr)

mergesort([5,4,3,2,1])