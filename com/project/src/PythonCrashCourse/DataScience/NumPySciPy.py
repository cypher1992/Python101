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

    def initDataFrame(self,data,index=None):
        if(index != None):
            return pd.DataFrame(data)
        else:
            return pd.DataFrame(data,index)

