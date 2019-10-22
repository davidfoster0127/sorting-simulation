

class BubbleSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "BubbleSort"
        print("Init BubbleSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        done = True
        temp = ''
        self.spaceUsed += 2

        while done:
            done = False
            for i in range(0, n - 1):
                if arr[i] > arr[i + 1]:
                    temp = arr[i + 1]
                    arr[i + 1] = arr[i]
                    arr[i] = temp
                    done = True
        return arr

