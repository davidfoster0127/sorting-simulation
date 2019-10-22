
class SortingData:

    # dataCategories = ["guids", "birthdays", "phonenumbers", "zip9s"]
    dataCategories = ["guids"]


    def __init__(self, dataSize):
        self.data = {}
        self.dataSize = dataSize

        for category in self.dataCategories:
            self.data[category] = {}

        self.loadData()
        print("Init SortingData")

    def loadData(self):
        print("Loading data...")

        for category in self.dataCategories:
            with open('data/'+category+'.txt') as dataFile:  # read in raw data
                lines = dataFile.readlines()
                self.data[category]["raw"] = lines[0:self.dataSize - 1]

        # maybe could read in files of different sortedness here or do some other processing on it
        # with open('data/guids_semisorted.txt') as dataFile:
        #     lines = dataFile.readlines()
        #     data["guids"] = lines[0:dataLength-1]

    def getRawDataSets(self):
        toReturn = {}

        for category in self.dataCategories:
            toReturn[category] = self.data[category]["raw"]

        return toReturn
