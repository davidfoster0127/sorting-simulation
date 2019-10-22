from matplotlib import pyplot
from functools import partial
import timeit
import math
import random
import numpy

import bubblesort
import insertionsort
import selectionsort
import quicksort
import mergesort
import sortingdata


def doRunsBySize(sorts, data):
    rawData = data.getRawDataSets()

    iterations = 5
    sizeChunks = 10

    dataSizes = []
    for dsize in range(0, data.dataSize + 1, math.floor(data.dataSize / sizeChunks)):
        if dsize == 0:
            dsize = 1
        dataSizes.append(dsize)

    results = {}
    for s in sorts:
        results[s.name] = {}
        for dname in data.dataCategories:
            results[s.name][dname] = {}
            for dsize in dataSizes:
                results[s.name][dname][dsize] = {}

    for dname in data.dataCategories:
        for s in sorts:
            for dsize in dataSizes:
                totaltime = 0
                for iteration in range(0, iterations):
                    print(f"Iteration {iteration} for {s.name} on {dname} of size {dsize}")
                    datacopy = rawData[dname].copy()
                    timer = timeit.Timer(partial(s.sort, datacopy[0:dsize]))
                    t = timer.timeit(1)
                    totaltime += t
                avg = totaltime / iterations
                results[s.name][dname][dsize]['time'] = avg
                results[s.name][dname][dsize]['space'] = s.spaceUsed

    return results


def displayResults(results):

    sortNames = []
    dataNames = []
    dataSizes = []

    for sname in results.keys():
        sortNames.append(sname)

    for dname in results[sortNames[0]].keys():
        dataNames.append(dname)

    for dsize in results[sortNames[0]][dataNames[0]].keys():
        dataSizes.append(dsize)

    for dname in dataNames:
        for sname in sortNames:
            averages = []
            for dsize in dataSizes:
                averages.append(results[sname][dname][dsize]['time'])

            pyplot.plot(dataSizes, averages, '-', label=sname)

        pyplot.title(f'{dname} runtime')
        pyplot.legend()
        pyplot.show()

    for dname in dataNames:
        for sname in sortNames:
            averages = []
            for dsize in dataSizes:
                averages.append(results[sname][dname][dsize]['space'])

            pyplot.plot(dataSizes, averages, '-', label=sname)

        pyplot.title(f'{dname} space used')
        pyplot.legend()
        pyplot.show()


def main():
    # read in data files
    # format data into sortable ready form

    # do every sort on each set of data, returning and collecting runtime and space used for each run

    # use output to create 16 graphs
    # 2 different y-axis,
        # runtime
        # space used
    # 2 different x-axis
        # data size
        # data sortedness
    # 4 different types of data
        # 2 synthetic distributions
            # bell curve
            # perfect?
        # 2 real world data sets
            # zipcodes
            # birthdate

    sdata = sortingdata.SortingData(1000)

    bsort = bubblesort.BubbleSort()
    isort = insertionsort.InsertionSort()
    ssort = selectionsort.SelectionSort()
    qsort = quicksort.QuickSort()
    msort = mergesort.MergeSort()

    sorts = [bsort, isort, ssort, qsort, msort]

    results = doRunsBySize(sorts, sdata)

    displayResults(results)


if __name__ == "__main__":
    main()

