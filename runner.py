from matplotlib import pyplot
from functools import partial
import timeit
import math
import json
import time
import numpy as np

import bubblesort
import insertionsort
import selectionsort
import quicksort
import mergesort
import sortingdata
import shuffle


def doRunsBySize(sorts, data):
    # grab the data from the SortingData object
    rawData = data.dataBySize

    # number of iterations we will get the average from
    avgIterations = 5

    # pre-create map entries, add the 0 data point
    results = {}
    for s in sorts:
        results[s.name] = {}
        for dname in data.dataSets:
            results[s.name][dname] = {}
            results[s.name][dname][0] = {}
            results[s.name][dname][0]['time'] = 0
            results[s.name][dname][0]['space'] = 0
            results[s.name][dname][0]['std'] = 0
            for dsize in data.dataSizes:
                results[s.name][dname][dsize] = {}

    # iterate over the datasets, the sorts, and data sizes and run each combination 5 times
    for dname in data.dataSets:
        for s in sorts:
            for dsize in data.dataSizes:
                totaltime = 0
                times = []
                for iteration in range(0, avgIterations):
                    print(f"Iteration {iteration} for {s.name} on {dname} of size {dsize}")
                    datacopy = rawData[dname][dsize].copy()
                    timer = timeit.Timer(partial(s.sort, datacopy))
                    t = timer.timeit(1)
                    times.append(t)
                    totaltime += t
                # calculate the average runtime and record it along with the spaceUsed and standard deviation
                avg = totaltime / avgIterations
                results[s.name][dname][dsize]['time'] = avg
                results[s.name][dname][dsize]['space'] = s.spaceUsed
                results[s.name][dname][dsize]['std'] = np.std(times)

    return results


def doRunsBySortedness(sorts, data):
    # grab the data from the SortingData object
    rawData = data.dataBySortedness

    # number of iterations we will get the average from
    avgIterations = 5

    # pre-create map entries
    results = {}
    for s in sorts:
        results[s.name] = {}
        for dname in data.dataSets:
            results[s.name][dname] = {}
            for sortedness in data.dataSortedness:
                results[s.name][dname][sortedness] = {}

    # iterate over the datasets, the sorts, and data sortedness and run each combination 5 times
    for dname in data.dataSets:
        for s in sorts:
            for sortedness in data.dataSortedness:
                totaltime = 0
                times = []
                for iteration in range(0, avgIterations):
                    print(f"Iteration {iteration} for {s.name} on {dname} of sortedness {sortedness}")
                    datacopy = rawData[dname][sortedness].copy()
                    timer = timeit.Timer(partial(s.sort, datacopy))
                    t = timer.timeit(1)
                    times.append(t)
                    totaltime += t
                # calculate the average runtime and record it along with the spaceUsed and standard deviation
                avg = totaltime / avgIterations
                results[s.name][dname][sortedness]['time'] = avg
                results[s.name][dname][sortedness]['space'] = s.spaceUsed
                results[s.name][dname][sortedness]['std'] = np.std(times)

    return results


def displayResults(results, fromfile=False):

    sortNames = []
    dataNames = []
    dataSizes = []

    # create arrays of the values to use for the plots (makes it easier to work with)
    for sname in results.keys():
        sortNames.append(sname)

    for dname in results[sortNames[0]].keys():
        dataNames.append(dname)

    for dsize in results[sortNames[0]][dataNames[0]].keys():
        dataSizes.append(dsize)

    pyplot.figure()
    subplot = 241

    # add the 4 runtime graphs to the figure
    for dname in dataNames:
        pyplot.subplot(subplot)
        subplot += 1
        for sname in sortNames:
            averages = []
            for dsize in dataSizes:
                if fromfile:
                    averages.append(results[sname][dname][str(dsize)]['time'])
                else:
                    averages.append(results[sname][dname][dsize]['time'])
            pyplot.plot(dataSizes, averages, '-', label=sname)
        pyplot.title(f'{dname} runtime')
        pyplot.legend()
        pyplot.grid(True)
        # pyplot.yscale('log')

    # add the 4 space used graphs to the figure
    for dname in dataNames:
        pyplot.subplot(subplot)
        subplot += 1
        for sname in sortNames:
            averages = []
            for dsize in dataSizes:
                if fromfile:
                    averages.append(results[sname][dname][str(dsize)]['space'])
                else:
                    averages.append(results[sname][dname][dsize]['space'])
            pyplot.plot(dataSizes, averages, '-', label=sname)
        pyplot.title(f'{dname} space used')
        pyplot.legend()
        pyplot.grid(True)

    # add some padding and show the graphs
    pyplot.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    pyplot.show()


def main():
    # create the data object and load the data from the files
    sdata = sortingdata.SortingData()

    # create instances of each sorting object
    bsort = bubblesort.BubbleSort()
    isort = insertionsort.InsertionSort()
    ssort = selectionsort.SelectionSort()
    qsort = quicksort.QuickSort()
    msort = mergesort.MergeSort()
    sorts = [bsort, isort, ssort, qsort, msort]

    # do runs by size, display the results, and record the results
    results = doRunsBySize(sorts, sdata)
    displayResults(results)  # this pauses the code execution so we typically leave one of these clocks to execute
    with open(f'results/results-bysize-{time.time()}.json', 'w') as file_object:
        json.dump(results, file_object)

    # do runs by sortedness, display the results, and record the results
    results = doRunsBySortedness(sorts, sdata)
    displayResults(results)
    with open(f'results/results-bysortedness-{time.time()}.json', 'w') as file_object:
        json.dump(results, file_object)

    # comment out the above code use this to display a specific results file
    # readAndDisplayResults('results/results-good-10k-sortedness.json')


def readAndDisplayResults(filename):
    with open(filename, 'r') as file_object:
        blob = json.load(file_object)

    displayResults(blob, True)


def generateSyntheticNumbers():
    # generate synthetic lognormal distributions with sizes from 1k-10k and record each result
    for n in range(1000, 10001, 1000):
        s = np.random.lognormal(3., 1., n)
        with open(f'data/synth-lognormal-{math.floor(n/1000)}k.txt', 'w') as file_object:
            for num in s:
                file_object.write(num.__str__()+'\n')

    # generate synthetic normal distributions with sizes from 1k-10k and record each result
    for n in range(1000, 10001, 1000):
        s = np.random.normal(100, 10, n)
        with open(f'data/synth-normal-{math.floor(n/1000)}k.txt', 'w') as file_object:
            for num in s:
                file_object.write(num.__str__()+'\n')


if __name__ == "__main__":
    # generateSyntheticNumbers()  # generated the synthetic numbers
    # shuffle.ShuffledData(10000, 1)  # generates the files with different levels of sortedness
    main()

