import pandas

class Statistics():
    def __init__(self,listOfVals):
        self.listOfVals = listOfVals

    def getList(self):
        return self.listOfVals

    def setListOfVals(self,newList):
        self.listOfVals = newList

    def arithmeticMean(self):
        if (len(self.listOfVals) > 0):
            total = 0
            for elements in self.listOfVals:
                total += elements
            length = len(self.listOfVals)
            return total/length
        else:
            return 0