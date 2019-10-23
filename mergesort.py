import math


class MergeSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "MergeSort"
        print("Init MergeSort")

    def sort(self, arr):
        self.spaceUsed = len(arr)
        self.mergesort(arr)

    def mergesort(self, arr):
        n = len(arr)

        half = n / 2
        self.spaceUsed += 1

        if n > 1:
            left = arr[:math.floor(half)]
            right = arr[math.floor(half):]
            self.spaceUsed += (len(left)+len(right))
            self.mergesort(left)
            self.mergesort(right)
            self.merge(arr, left, right)

        return arr

    def merge(self, arr, left, right):
        i = 0
        j = 0
        k = 0
        self.spaceUsed += 3

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            k = k + 1
            i = i + 1
        while j < len(right):
            arr[k] = right[j]
            k = k + 1
            j = j + 1

        return arr
