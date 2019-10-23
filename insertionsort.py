

class InsertionSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "InsertionSort"
        print("Init InsertionSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        for nextPos in range(1, n):
            self.insert(arr, nextPos)

        return arr

    def insert(self, arr, nextPos):
        nextValue = arr[nextPos]
        self.spaceUsed += 1

        while nextPos > 0 and nextValue < arr[nextPos - 1]:
            arr[nextPos] = arr[nextPos - 1]
            nextPos = nextPos - 1

        arr[nextPos] = nextValue
