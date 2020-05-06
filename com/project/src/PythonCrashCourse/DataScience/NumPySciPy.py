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
        npArray = self.numpyArray(array)
        return np.mean(array)

    def scipyNPV(self,array,rate):
        return round(sp.npv(rate,array),2)