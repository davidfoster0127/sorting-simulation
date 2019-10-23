import math


class SortingData:

    # the different data types we test on
    dataSets = ["real-dates", "real-ids", "synth-lognormal", "synth-normal"]

    # the dataSizes we test on and the file names for each size
    dataSizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    fileSizes = ['1k', '2k', '3k', '4k', '5k', '6k', '7k', '8k', '9k', '10k']

    # the dataSortedness we test on and the file names for each size
    dataSortedness = [0.1, 0.3, 0.5, 0.7, 0.9, 1]
    fileSortedness = ['0.1_', '0.3_', '0.5_', '0.7_', '0.9_', 'fully_']

    def __init__(self):
        print("Init SortingData")

        self.dataBySize = {}
        self.dataBySortedness = {}

        # load all of the data into the SortingData object from files
        self.loadDataBySize()
        self.loadDataBySortedness()

    def loadDataBySize(self, size=10000, intervals=10):
        print("Loading data by size...")

        dataIntervalSize = math.floor(size/intervals)
        self.dataSizes = []
        for i in range(dataIntervalSize, size+1, dataIntervalSize):
            self.dataSizes.append(i)

        for dset in self.dataSets:
            self.dataBySize[dset] = {}
            for i in range(len(self.fileSizes)):
                with open(f'data/{dset}-{self.fileSizes[i]}.txt', 'r') as dataFile:
                    lines = dataFile.readlines()
                    self.dataBySize[dset][self.dataSizes[i]] = lines[0:self.dataSizes[i]]

    def loadDataBySortedness(self, size=10000):
        print("Loading data by sortedness...")

        for dset in self.dataSets:
            self.dataBySortedness[dset] = {}
            for i in range(len(self.fileSortedness)):
                with open(f'data/{dset}-10k_{self.fileSortedness[i]}sorted.txt', 'r') as dataFile:
                    lines = dataFile.readlines()
                    self.dataBySortedness[dset][self.dataSortedness[i]] = lines[0:size]
