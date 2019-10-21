from matplotlib import pyplot
from functools import partial
import timeit
import random
import numpy

from bubblesort import bubblesort, bubblesort2
from quicksort import quicksortstarter
from mergesort import mergesort
from selectionsort import selectionsort
from insertionsort import insertionsort, insertionsort2


def test(arr):
    return 0


def plotTC(fn, nTests):
    x = []
    y = []
    arr = []
    for j in range(0, 25):
        arr.append(j)

    arr.reverse()
    for i in range(0, nTests):
        arr2 = arr.copy()
        testNTimer = timeit.Timer(partial(fn, arr2))
        t = testNTimer.timeit(number=1)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')

def getAvgRuntime(fn, data, iterations=5):

    times = []

    for i in range(0, iterations):
        cp = data.copy()
        timer = timeit.Timer(partial(fn, cp))
        t = timer.timeit(1)
        times.append(t)

    total = 0
    for ti in times:
        total += ti
    avg = total/len(times)

    print("times = "+str(times))
    return avg



def main():
    with open('data/guids.txt') as dataFile:
        lines = dataFile.readlines()

    

    dataSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] # reasonable sizes
    averages = []

    for size in dataSizes:
        avg = getAvgRuntime(bubblesort, lines[0:size])
        averages.append(avg)
    p1 = pyplot.plot(dataSizes, averages, '-', label='bubble')

    averages = []

    for size in dataSizes:
        avg = getAvgRuntime(insertionsort, lines[0:size])
        averages.append(avg)
    p2 = pyplot.plot(dataSizes, averages, '-', label='insert')

    averages = []

    for size in dataSizes:
        avg = getAvgRuntime(selectionsort, lines[0:size])
        averages.append(avg)
    p3 = pyplot.plot(dataSizes, averages, '-', label='selection')

    averages = []

    for size in dataSizes:
        avg = getAvgRuntime(quicksortstarter, lines[0:size])
        averages.append(avg)
    p4 = pyplot.plot(dataSizes, averages, '-', label='quick')

    averages = []

    for size in dataSizes:
        avg = getAvgRuntime(mergesort, lines[0:size])
        averages.append(avg)
    p4 = pyplot.plot(dataSizes, averages, '-', label='merge')


    pyplot.legend()
    pyplot.show()


    # read in data files
    # format data into sortable ready form

    # do every sort on each set of data, returning and collecting runtime and space used for each run

    # use output to create 16 graphs

    # 2 different y-axis, runtime and space used
    # 2 different x-axis, data size and data sortedness
    # 4 different types of data
    # 2 synthetic distributions
    # bell curve
    # perfect
    # 2 real world data sets
    # zipcodes
    # birthdate

    # plotTC(bubblesort, 50)
    # plotTC(quicksortstarter, 10)
    # plotTC(mergesort, 10)
    # plotTC(insertionsort, 10)
    # plotTC(selectionsort, 10)
    # pyplot.show()

if __name__ == "__main__":
    main()


def produceDataFiles():
    filename = 'data/convertcsv.csv'
    with open(filename) as dataFile:
        lines = dataFile.readlines()

    guid = []
    phones = []
    zip9 = []
    birthday = []

    lineN = 1
    while lineN < len(lines) - 1:
        parts = lines[lineN].split(',')
        guid.append(parts[0])
        phones.append(parts[1])
        zip9.append(parts[2])
        birthday.append(parts[3][0:-1])
        lineN += 1

    filename = 'data/guids.txt'
    with open(filename, 'w') as file_object:
        for line in guid:
            file_object.write(line)
            file_object.write('\n')

    filename = 'data/phonenumbers.txt'
    with open(filename, 'w') as file_object:
        for line in phones:
            file_object.write(line)
            file_object.write('\n')

    filename = 'data/zip9s.txt'
    with open(filename, 'w') as file_object:
        for line in zip9:
            file_object.write(line)
            file_object.write('\n')

    filename = 'data/birthdays.txt'
    with open(filename, 'w') as file_object:
        for line in birthday:
            file_object.write(line)
            file_object.write('\n')