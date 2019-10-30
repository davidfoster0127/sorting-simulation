import pylab
from random import shuffle

def selectionsort_visualized(arr):
    x = range(len(arr))
    imgidx = 0
    posMin = 0

    for fill in range(len(arr) -1):
        posMin = fill
        for next in range(fill + 1, len(arr) -1):
            if (arr[next] < arr[posMin]):
                posMin = next
        arr[fill], arr[posMin] = arr[posMin], arr[fill]

        pylab.plot(x,arr,'k.',markersize=6)
        pylab.savefig("selectionsort/image" + '%04d' % imgidx + ".png")
        pylab.clf() 
        imgidx = imgidx + 1

arr = list(range(300))
shuffle(arr)
selectionsort_visualized(arr)

