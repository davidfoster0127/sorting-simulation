import pylab
from random import shuffle

def bubblesort_visualized(arr):
    x = range(len(arr))
    imgidx = 0
    done = True
    while done:
        done = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = True

        pylab.plot(x,arr,'k.',markersize=6)
        pylab.savefig("bubblesort/imgage" + '%04d' % imgidx + ".png")
        pylab.clf() 
        imgidx = imgidx + 1

arr = list(range(300))
shuffle(arr)
bubblesort_visualized(arr)
