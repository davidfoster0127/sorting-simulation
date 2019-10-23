import numpy as np
import random
from math import floor

class ShuffledData:

    #dataCategories = ["guids", "birthdays", "phonenumbers", "zip9s"]
    #dataCategories = ["synth-lognormal-5k", "real-ids-5k", "synth-normal-5k",]
    dataCategories = ["synth-lognormal-10k", "real-ids-10k", "synth-normal-10k","real-dates-10k"]
    def __init__(self, dataSize, inversionPerctage):
        self.data = {}
        self.dataSize = dataSize
        self.inversionPerctage = (inversionPerctage % 10) / 10

 
    def loadShuffledData(self): 
        
        for category in self.dataCategories:
            arr = []
            with open('data/'+category+'.txt') as dataFile:
                lines = dataFile.readlines()
                arr = [currentfile for currentfile in lines[0:self.dataSize - 1]]
                arr.sort(reverse=True)
                arr = self.randomize(arr)
            with open('data/'+category+'_'+str(self.inversionPerctage)+'_sorted.txt',"w+") as  file:
                for line in arr:
                    file.write(line)
        
    def randomize(self,arr):
        n = len(arr)
        y = floor(n * self.inversionPerctage) + 1
        x = floor(n* (1 - self.inversionPerctage))

        result = sorted(arr[n - x:len(arr)]) + arr[0:y+1]

          
        return result

    def getInvCount(self, arr): 
        n = len(arr)
        inv_count = 0
        for i in range(n): 
            for j in range(i + 1, n): 
                if (arr[i] > arr[j]): 
                    inv_count += 1
    
        return inv_count 
  
ShuffledData(10000, 3).loadShuffledData()