
def quicksort(arr, left, right):
    i = left 
    j = right
    floor = int((left + right) /2)
    pivot = arr[floor]

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot: 
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i +=1
            j -= 1
    
    if left < j :
        quicksort(arr, left, j)
    if i < right:
        quicksort(arr, i, right)


def quicksortstarter(arr):

    quicksort(arr, 0, len(arr) -1 )
    return arr


print(quicksortstarter([5,4,3,2,1]))
