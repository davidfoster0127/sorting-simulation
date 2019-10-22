
def selectionsort (arr):
    n = len(arr)
    for fill in range(0, n):
        posMin = fill
        for next in range(fill + 1, n):
            if(arr[next] < arr[posMin]):
                posMin = next
        arr[fill], arr[posMin] = arr[posMin], arr[fill]
        
    return arr

print(selectionsort([5,4,3,2,1]))



class SelectionSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "SelectionSort"
        print("Init SelectionSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        temp = ''
        posMin = 0
        self.spaceUsed += 2

        for fill in range(0, n):
            posMin = fill

            for next in range(fill + 1, n):
                if (arr[next] < arr[posMin]):
                    posMin = next

            temp = arr[fill]
            arr[fill] = arr[posMin]
            arr[posMin] = temp

        return arr
