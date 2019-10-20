from matplotlib import pyplot
from functools import partial
import timeit
import random
import numpy

import bubblesort

def test(arr):
    return 0
def plotTC(fn, nMin, nMax, nInc, nTests):

    x = []
    y = []
    arr = []
    for j in range(0, 1000):
        arr.append(j)
    arr.reverse() 
    for i in range(0, 1000):   
        testNTimer = timeit.Timer(partial(fn, arr))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')
    pyplot.legend([p1,], [fn.__name__, ])

def main():

    plotTC(bubblesort.bubblesort, 10, 1000, 10, 10)

    pyplot.show()

if __name__ == "__main__":
    main()    