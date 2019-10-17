def insertionsort(arr):
    n = len(arr)
    for nextPos in range(1, n):
        insert(arr, nextPos)
    return arr 
def insert(arr, nextPos):
    nextValue = arr[nextPos]
    while nextPos > 0 and nextValue < arr[nextPos-1] : 
        arr[nextPos] = arr[nextPos -1]
        nextPos = nextPos - 1
    arr[nextPos] = nextValue

print(insertionsort([5,1,2,4,6]))

    