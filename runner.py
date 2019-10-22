from matplotlib import pyplot
from functools import partial
import timeit
import math
import json
import random
import numpy as np

import bubblesort
import insertionsort
import selectionsort
import quicksort
import mergesort
import sortingdata


def doRunsBySize(sorts, data):
    rawData = data.dataBySize

    avgIterations = 5

    results = {}
    for s in sorts:
        results[s.name] = {}
        for dname in data.dataSets:
            results[s.name][dname] = {}
            results[s.name][dname][0] = {}
            results[s.name][dname][0]['time'] = 0
            results[s.name][dname][0]['space'] = 0
            for dsize in data.dataSizes:
                results[s.name][dname][dsize] = {}


    for dname in data.dataSets:
        for s in sorts:
            for dsize in data.dataSizes:
                totaltime = 0
                for iteration in range(0, avgIterations):
                    print(f"Iteration {iteration} for {s.name} on {dname} of size {dsize}")
                    datacopy = rawData[dname][dsize].copy()
                    timer = timeit.Timer(partial(s.sort, datacopy))
                    t = timer.timeit(1)
                    totaltime += t
                avg = totaltime / avgIterations
                # TODO: calculate standard deviation
                results[s.name][dname][dsize]['time'] = avg
                results[s.name][dname][dsize]['space'] = s.spaceUsed
                # TODO: maybe output stats here instead of at the end

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

        pyplot.yscale('log')
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
            # normal
            # lognormal
        # 2 real world data sets
            # zipcodes
            # birthdate

    sdata = sortingdata.SortingData()

    bsort = bubblesort.BubbleSort()
    isort = insertionsort.InsertionSort()
    ssort = selectionsort.SelectionSort()
    qsort = quicksort.QuickSort()
    msort = mergesort.MergeSort()

    sorts = [bsort, isort, ssort, qsort, msort]

    results = doRunsBySize(sorts, sdata)

    displayResults(results)

    with open('results1.json', 'w') as file_object:
        json.dump(results, file_object)


def generateSyntheticNumbers():
    mu, sigma = 3., 1.
    # s = np.random.lognormal(mu, sigma, 10000)

    # count, bins, ignored = pyplot.hist(s, 100, normed=True, align='mid')
    # x = np.linspace(min(bins), max(bins), 10000)
    # pdf = (np.exp(-(np.log(x) - mu) ** 2 / (2 * sigma ** 2))
    #              / (x * sigma * np.sqrt(2 * np.pi)))
    # pyplot.plot(x, pdf, linewidth=2, color='r')
    # pyplot.axis('tight')
    # pyplot.show()

    for n in range(1000, 10001, 1000):
        s = np.random.lognormal(mu, sigma, n)

        with open(f'data/synth-lognormal-{math.floor(n/1000)}k.txt', 'w') as file_object:
            for num in s:
                file_object.write(num.__str__()+'\n')


if __name__ == "__main__":
    # generateSyntheticNumbers()
    main()

