def selectionsort(arr):
    n = len(arr)
    for fill in range(0, n):
        posMin = fill
        for next in range(fill + 1, n):
            if(arr[next] < arr[posMin]):
                posMin = next
        temp = arr[fill]
        arr[fill] = arr[posMin]
        arr[posMin] = temp
    return arr

# print(selectionsort([5,4,3,2,1]))