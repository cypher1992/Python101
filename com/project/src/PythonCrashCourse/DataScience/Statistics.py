import pandas

class Statistics():
    def __init__(self,listOfVals):
        self.listOfVals = listOfVals

    def getListOfVals(self):
        return self.listOfVals

    def setListOfVals(self,newList):
        self.listOfVals = newList