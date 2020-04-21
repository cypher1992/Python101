import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Statistics():
    def __init__(self,listOfVals):
        self.listOfVals = listOfVals

    def getList(self):
        return self.listOfVals

    def setListOfVals(self,newList):
        self.listOfVals = newList

    def plotData(self,yaxisLabel = "Y-Axis"):
        plt.plot(self.getList())
        plt.ylabel(yaxisLabel)
        plt.show()

    def plotDataMean(self,yaxisLabel = "Y-Axis"):
        plt.plot(self.getList())
        plt.plot([self.arithmeticMean()])
        plt.ylabel(yaxisLabel)
        plt.show()

    def rangeList(self):
        if(len(self.getList()) >0):
            maxVal = max(self.listOfVals)
            minVal = min(self.listOfVals)
            return maxVal-minVal
        else:
            return None

    def mode(self):
        statDict = {}
        modeValue = None
        if len(self.getList()) != 0:
            for index in self.getList():
                if index in statDict:
                    currentCount = statDict.get(index)
                    statDict[index] = currentCount+1
                else:
                    statDict[index] = 1
            statList = sorted(statDict.items(), key=  lambda kv:(kv[1],kv[0]))
            modeValue = statList[len(statDict)-1][0]
        return modeValue

    def median(self):
        length = len(self.getList())
        if(length != 0):
            if(length%2 == 0):
                middleIndex = int((length/2)-1)
                indexMed =  self.getList()[middleIndex]
                indexMed2 = self.getList()[middleIndex+1]
                return (indexMed+indexMed2)/2
            else:
                position = math.ceil(length/2)-1
                return self.getList()[position]
        else:
            return None

    def arithmeticMean(self):
        if (len(self.listOfVals) > 0):
            total = 0
            for elements in self.listOfVals:
                total += elements
            length = len(self.listOfVals)
            return total/length
        else:
            return 0

    def geometricMean(self):
        length = len(self.listOfVals)
        if(length >0):
            total = 1
            for index in self.listOfVals:
                total *= index
            return total**(1/length)
        else:
            return 0

    def harmonicMean(self):
        if(0 in self.listOfVals or len(self.listOfVals) == 0):
            return None
        else:
            length = len(self.listOfVals)
            total = 0
            for index in self.listOfVals:
                total += (1/index)
            return length/total

    def meanAbsoluteDeviation(self):
        if(len(self.getList())!= 0):
            mean = self.arithmeticMean()
            total = 0
            for index in self.getList():
                total += abs(mean-index)
            return  total/len(self.getList())
        else:
            None

    def variance(self,population=True):
        size = len(self.getList())
        if(size != 0):
            mean = self.arithmeticMean()
            total = 0
            for index in self.getList():
                total+=(mean-index)**2
            if(population):
                return total/size
            else:
                return total/(size-1)
        else:
            return None

    def standardDeviation(self,population=True):
        if(len(self.getList()) != 0):
            if(population):
                return self.variance()**(0.5)
            else:
                return self.variance(population=False)**(0.5)
        else:
            return None

    def chebyshevInequality(self):
        if(len(self.getList()) != 0):
            std = self.standardDeviation()
            if(std < 1):
                return None
            else:
                return 1- (1.0/std**2)
        else:
            return None

    def zscore(self):
        list = []
        for i in self.getList():
            list.append((i - self.arithmeticMean()) / self.standardDeviation())
        return list