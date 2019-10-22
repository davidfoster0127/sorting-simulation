import math


class SortingData:

    dataSets = ["real-dates", "real-ids", "synth-lognormal", "synth-normal"]

    maxDataSize = 10000
    dataIntervals = 10
    dataIntervalSize = 1000
    dataSizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    fileSizes = ['1k', '2k', '3k', '4k', '5k', '6k', '7k', '8k', '9k', '10k']

    def __init__(self):
        print("Init SortingData")

        self.dataBySize = {}
        self.loadDataBySize(10000)


    def loadDataBySize(self, maxSize):
        print("Loading data by size...")

        if maxSize != self.maxDataSize:
            self.dataIntervalSize = math.floor(maxSize/self.dataIntervals)
            self.dataSizes = []
            for i in range(self.dataIntervalSize,maxSize+1, self.dataIntervalSize):
                self.dataSizes.append(i)
        print(self.dataSizes)

        for dset in self.dataSets:
            self.dataBySize[dset] = {}
            for i in range(len(self.fileSizes)):
                with open(f'data/{dset}-{self.fileSizes[i]}.txt', 'r') as dataFile:
                    lines = dataFile.readlines()
                    self.dataBySize[dset][self.dataSizes[i]] = lines[0:self.dataSizes[i]]
