from math import floor


class ShuffledData:

    dataCategories = ["synth-lognormal-10k", "real-ids-10k", "synth-normal-10k","real-dates-10k"]

    def __init__(self, dataSize, inversionPercentage):
        self.data = {}
        self.dataSize = dataSize
        self.inversionPercentage = (inversionPercentage % 10) / 10

        # generates the files with different levels of sortedness
        self.loadShuffledData()
        self.loadFullySorted()

    def loadFullySorted(self):
        for category in self.dataCategories:
            with open('data/'+category+'.txt') as dataFile:
                lines = dataFile.readlines()
                arr = [currentfile for currentfile in lines[0:self.dataSize - 1]]
                arr.sort()
            with open('data/'+category+'_fully_sorted.txt',"w+") as  file:
                for line in arr:
                    file.write(line)

    def loadShuffledData(self): 
        
        for category in self.dataCategories:
            arr = []
            with open('data/'+category+'.txt') as dataFile:
                lines = dataFile.readlines()
                arr = [currentfile for currentfile in lines[0:self.dataSize - 1]]
                arr.sort(reverse=True)
                arr = self.randomize(arr)
            with open('data/'+category+'_'+str(self.inversionPercentage)+'_sorted.txt' , "w+") as file:
                for line in arr:
                    file.write(line)

    def randomize(self,arr):
        n = len(arr)
        y = floor(n * self.inversionPercentage) + 1
        x = floor(n * (1 - self.inversionPercentage))

        result = sorted(arr[n - x:len(arr)]) + arr[0:y+1]

        return result

    def getInvCount(self, arr): 
        n = len(arr)
        inv_count = 0
        for i in range(n): 
            for j in range(i + 1, n): 
                if arr[i] > arr[j]:
                    inv_count += 1
    
        return inv_count
