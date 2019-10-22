import math


class QuickSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "QuickSort"
        print("Init QuickSort")

    def sort(self, arr):
        self.spaceUsed = len(arr)
        self.quicksort(arr, 0, len(arr) - 1)

    def quicksort(self, arr, left, right):
        i = left
        j = right
        floor = math.floor((left + right) / 2)
        pivot = arr[floor]
        temp = ''
        self.spaceUsed += 6

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

        if left < j:
            self.quicksort(arr, left, j)
        if i < right:
            self.quicksort(arr, i, right)
