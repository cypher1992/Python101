import pandas
import math

class Statistics():
    def __init__(self,listOfVals):
        self.listOfVals = listOfVals

    def getList(self):
        return self.listOfVals

    def setListOfVals(self,newList):
        self.listOfVals = newList

    def rangeList(self):
        if(len(self.getList()) >0):
            maxVal = max(self.listOfVals)
            minVal = min(self.listOfVals)
            return maxVal-minVal
        else:
            return None

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