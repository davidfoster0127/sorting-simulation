def bubblesort(arr):
    n = len(arr)
    cPass = 1
    done = True

    while done:
        done = False
        for i in range(0, n - cPass):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                done = True
    return arr            
print(bubblesort([5,4,3,2,1]))