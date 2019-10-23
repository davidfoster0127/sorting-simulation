from matplotlib import pyplot
from functools import partial
import timeit
import math
import json
import time
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
            results[s.name][dname][0]['std'] = 0
            for dsize in data.dataSizes:
                results[s.name][dname][dsize] = {}


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
                avg = totaltime / avgIterations
                results[s.name][dname][dsize]['time'] = avg
                results[s.name][dname][dsize]['space'] = s.spaceUsed
                results[s.name][dname][dsize]['std'] = np.std(times)

    return results


def doRunsBySortedness(sorts, data):
    rawData = data.dataBySortedness

    avgIterations = 5

    results = {}
    for s in sorts:
        results[s.name] = {}
        for dname in data.dataSets:
            results[s.name][dname] = {}
            for sortedness in data.dataSortedness:
                results[s.name][dname][sortedness] = {}


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
                avg = totaltime / avgIterations
                results[s.name][dname][sortedness]['time'] = avg
                results[s.name][dname][sortedness]['space'] = s.spaceUsed
                results[s.name][dname][sortedness]['std'] = np.std(times)

    return results


def displayResults(results, fromfile=False):

    sortNames = []
    dataNames = []
    dataSizes = []

    for sname in results.keys():
        sortNames.append(sname)

    for dname in results[sortNames[0]].keys():
        dataNames.append(dname)

    for dsize in results[sortNames[0]][dataNames[0]].keys():
        dataSizes.append(dsize)

    pyplot.figure()
    subplot = 241

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
        pyplot.yscale('log')

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

    pyplot.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    pyplot.show()


def main():
    sdata = sortingdata.SortingData()

    bsort = bubblesort.BubbleSort()
    isort = insertionsort.InsertionSort()
    ssort = selectionsort.SelectionSort()
    qsort = quicksort.QuickSort()
    msort = mergesort.MergeSort()

    sorts = [bsort, isort, ssort, qsort, msort]

    results = doRunsBySize(sorts, sdata)
    displayResults(results)
    with open(f'results/results-bysize-{time.time()}.json', 'w') as file_object:
        json.dump(results, file_object)

    results = doRunsBySortedness(sorts, sdata)
    displayResults(results)
    with open(f'results/results-bysortedness-{time.time()}.json', 'w') as file_object:
        json.dump(results, file_object)

    # readAndDisplayResults()


def readAndDisplayResults():
    # with open(f'results/results-good-10k-size.json', 'r') as file_object:
    #     blob = json.load(file_object)
    with open(f'results/results-good-10k-sortedness.json', 'r') as file_object:
        blob = json.load(file_object)

    displayResults(blob, True)


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

