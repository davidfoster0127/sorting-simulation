from matplotlib import pyplot
from functools import partial
import timeit
import random
import numpy

from bubblesort import bubblesort
from quicksort import quicksortstarter
from mergesort import mergesort
from selectionsort import selectionsort
from insertionsort import insertionsort

def test(arr):
    return 0
def plotTC(fn, nTests):

    x = []
    y = []
    arr = []
    for j in range(0, 25):
        arr.append(j)
        
    arr.reverse() 
    for i in range(0, 1000):   
        testNTimer = timeit.Timer(partial(fn, arr))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')
  

def main():

    plotTC(bubblesort, 10)
    plotTC(quicksortstarter, 10)
    plotTC(mergesort, 10)
    plotTC(insertionsort, 10)
    plotTC(selectionsort, 10)
    pyplot.show()

if __name__ == "__main__":
    main()    