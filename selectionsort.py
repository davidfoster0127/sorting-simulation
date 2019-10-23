

class SelectionSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "SelectionSort"
        print("Init SelectionSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        posMin = 0
        self.spaceUsed += 1

        for fill in range(0, n):
            posMin = fill
            for next in range(fill + 1, n):
                if (arr[next] < arr[posMin]):
                    posMin = next
            arr[fill], arr[posMin] = arr[posMin], arr[fill]

        return arr
