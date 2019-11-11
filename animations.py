
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def insertionsort(arr):
    n = len(arr)

    for nextPos in range(1, n):
        yield from insert(arr, nextPos)

def insert(arr, nextPos):
    nextValue = arr[nextPos]

    while nextPos > 0 and nextValue < arr[nextPos - 1]:
        arr[nextPos] = arr[nextPos - 1]
        nextPos = nextPos - 1
        yield arr
    arr[nextPos] = nextValue
    

def bubblesort(arr):
    n = len(arr)

    done = True


    while done:
        done = False
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = True
                yield arr
    return arr
def selectionsort(arr):
    n = len(arr)

    posMin = 0

    for fill in range(0, n):
        posMin = fill
        for next in range(fill + 1, n):
            if (arr[next] < arr[posMin]):
                posMin = next
        arr[fill], arr[posMin] = arr[posMin], arr[fill]
        yield arr

def quicksort(arr, left, right):
    i = left
    j = right
    floor = math.floor(left + ((right - left + 1) // 2) - 1)
    pivot = arr[floor]

    if (left >= right):
        return

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
            yield arr

    if left < j:
        yield from quicksort(arr, left, j)
    if i < right:
        yield from quicksort(arr, i, right)

def mergesort(arr, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    yield from mergesort(arr, start, mid)

    yield from mergesort(arr, mid + 1, end)

    yield from merge(arr, start, mid, end)

    yield arr

def merge(arr, start, mid, end):

    array_after_merge = []

    left = start

    right = mid + 1

    while left <= mid and right <= end:

        if arr[left] < arr[right]:

            array_after_merge.append(arr[left])

            left += 1

        else:
            array_after_merge.append(arr[right])

            right += 1

    while left <= mid:

        array_after_merge.append(arr[left])

        left += 1

    while right <= end:

        array_after_merge.append(arr[right])

        right += 1

    for i, val in enumerate(array_after_merge):

        arr[start + i] = val

        yield arr
    
if __name__ == "__main__":

    size = int(input("Enter the size of your array:"))

    method = int(input("Sorting algoritym: {1: Insertion} {2: Selection}{3: Bubble}{4: Quick}{5: Merge}"))
    
    arr = list(range(size))
   
    random.seed(time.time())

    random.shuffle(arr)

    if method == 1:
        generator = insertionsort(arr)
        title = "Insertion sort"
    elif method  == 2:
        generator = selectionsort(arr)
        title = "Selection sort"
    elif method  == 3:    
        generator = bubblesort(arr)
        title = "Bubble sort"
    elif method  == 4:    
        generator = quicksort(arr, 0, len(arr) - 1)
        title = "Quick sort"
    elif method  == 5:       
        generator = mergesort(arr, 0, len(arr) -1)
        title = "Merge sort"

    fig, axis = plt.subplots()

    axis.set_title(title)

    bar = axis.bar(range(len(arr)), arr, align="edge")
    
    axis.set_xlim(0, len(arr))

    count = [0]

    def update_fig(arr, rects, count):

        for rect, val in zip(rects, arr):

            rect.set_height(val)
            
        count[0] += 1

    merge_visualization = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar, count), frames=generator, interval=1,
        repeat=False)

    plt.show()

