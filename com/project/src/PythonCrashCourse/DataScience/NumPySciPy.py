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

    def filterColumnDF(self, dataframe,columnFilter,filterValue):
        return (dataframe[columnFilter] ==  filterValue)