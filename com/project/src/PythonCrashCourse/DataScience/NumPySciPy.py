import numpy as np
import scipy as sp
import pandas as pd

class NumpySciPy:
    def __init__(self):
        pass

    def numpyArray(self,*array):
        npArray =np.array(array[0])
        return npArray

    def numpySize(self,*array):
        npArray =self.numpyArray(array)
        size = np.size(npArray)
        return size

    def numpyAverage(self,*array):
        return np.mean(array)

    def numpyCorrelate(self,*array):
        for arr in array:
            if(len(arr) == 2):
                return np.correlate(arr[0],arr[1])
            else:
                return None

    def numpySTD(self,*array):
        npArray = self.numpyArray(array)
        return np.std(npArray)

    def numpyNPV(self,array,rate):
        return round(np.npv(rate,array),2)

    def initDataFrame(self,data,rows=None):
        return pd.DataFrame(data,index=rows)

    def initSeries(self,array):
        return pd.Index(array)

    def headDF(self,dataframe):
        return dataframe.head()

    def tailDF(self,dataframe,numOfRows=10):
        return dataframe.tail(numOfRows)

    def infoDF(self,dataframe):
        return dataframe.info()

    def appendDF(self,dataframe,appendDataFrame):
        return dataframe.append(appendDataFrame)

    def dropDuplicatesDF(self,dataframe):
        return dataframe.drop_duplicates()

    def averageDF(self,dataframe):
        return dataframe.mean()

    def countDF(self,dataframe):
        return dataframe.count()
    
    def valueCountSeries(self,series):
        return series.value_counts()

    def corrDF(self,dataframe):
        return dataframe.corr()

    def filterColumnDF(self, dataframe,columnFilter,filterValue,):
        return dataframe[dataframe[columnFilter] == filterValue]

    def notFilterColumnDF(self, dataframe,columnFilter,filterValue):
        return dataframe[dataframe[columnFilter] != filterValue]

    def greaterThanFilterColumnDF(self, dataframe,columnFilter,filterValue):
        return dataframe[dataframe[columnFilter] > filterValue]

    def lessThanFilterColumnDF(self, dataframe,columnFilter,filterValue):
        return dataframe[dataframe[columnFilter] < filterValue]

    def greaterThanEqualsFilterColumnDF(self, dataframe,columnFilter,filterValue):
        return dataframe[dataframe[columnFilter] >= filterValue]

    def lessThanEqualsFilterColumnDF(self, dataframe,columnFilter,filterValue):
        return dataframe[dataframe[columnFilter] <= filterValue]

    def filterColumnDFAdv(self,dataframe,columnFilter,filterValue,filterType="EQUALS"):
        if(filterType == "EQUALS"):
            return self.filterColumnDF(dataframe=dataframe,columnFilter=columnFilter,filterValue=filterValue)
        elif(filterType == "NOT_EQUALS"):
            return self.notFilterColumnDF(dataframe=dataframe, columnFilter=columnFilter, filterValue=filterValue)
        elif (filterType == "GREATER_THAN"):
            return self.greaterThanFilterColumnDF(dataframe=dataframe, columnFilter=columnFilter, filterValue=filterValue)
        elif (filterType == "LESS_THAN"):
            return self.lessThanFilterColumnDF(dataframe=dataframe, columnFilter=columnFilter, filterValue=filterValue)
        elif (filterType == "GREATER_THAN_EQUALS"):
            return self.greaterThanEqualsFilterColumnDF(dataframe=dataframe, columnFilter=columnFilter, filterValue=filterValue)
        elif (filterType == "LESS_THAN_EQUALS"):
            return self.lessThanEqualsFilterColumnDF(dataframe=dataframe, columnFilter=columnFilter, filterValue=filterValue)
        else:
            return None

    def filterColumnAndOR(self,dataframe,columnFilter,filterValues,filterType=0):
        if filterType == 0:
            return dataframe[(dataframe[columnFilter] == filterValues[0]) | (dataframe[columnFilter] == filterValues[1])]
        else:
            return dataframe[
                (dataframe[columnFilter] == filterValues[0]) & (dataframe[columnFilter] == filterValues[1])]