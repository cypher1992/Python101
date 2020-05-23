import unittest
import numpy as np
import scipy as sp
import pandas as pd
from com.project.src.PythonCrashCourse.DataScience.NumPySciPy import NumpySciPy


class NumpySciPyTestClass(unittest.TestCase):

    def test_emptyArrayNumpyArray_returns_array(self):
        npsp = NumpySciPy()
        arrays = []
        actual = npsp.numpyArray(arrays)
        expected = np.array(arrays)
        boolArray= actual == expected
        isTrue =None
        if False in boolArray:
            isTrue = False
        else:
            isTrue = True
        self.assertTrue(isTrue)

    def test_emptyArrayNumpyArray_returns_array(self):
        npsp = NumpySciPy()
        arrays = [1]
        actual = npsp.numpyArray(arrays)
        expected = np.array(arrays)
        boolArray= actual == expected
        isTrue =None
        if False in boolArray:
            isTrue = False
        else:
            isTrue = True
        self.assertTrue(isTrue)

    def test_numpyArray_returns_array(self):
        npsp = NumpySciPy()
        arrays = [[1,2,3],[3,4,6]]
        actual = npsp.numpyArray(arrays)
        expected = np.array(arrays)
        boolArray= actual == expected
        isTrue =None
        if False in boolArray:
            isTrue = False
        else:
            isTrue = True
        self.assertTrue(isTrue)

    def testNumpySizeEmptyArray_returns_size0(self):
        npsy = NumpySciPy()
        emptyArray = []
        actual = npsy.numpySize(emptyArray)
        expected = 0
        self.assertEqual(expected,actual)

    def testNumpySizeArray1_returns_size1(self):
        npsy = NumpySciPy()
        emptyArray = [[1]]
        actual = npsy.numpySize(emptyArray)
        expected = 1
        self.assertEqual(expected, actual)


    def testNumpySizeArray3_returns_size1(self):
        npsy = NumpySciPy()
        emptyArray = [[1],[2],[3]]
        actual = npsy.numpySize(emptyArray)
        expected = 3
        self.assertEqual(expected, actual)

#Need to test return nan
    def testNumpyAverageEmptyArray(self):
        npsy = NumpySciPy()
        emptyArray = []
        isNaN = np.isnan(npsy.numpyAverage(emptyArray))
        self.assertTrue(isNaN)

    def testNumpyAveragetwoValueArray(self):
        npsy = NumpySciPy()
        emptyArray = [[1,2]]
        actual = npsy.numpyAverage(emptyArray)
        expected = 1.5
        self.assertEqual(expected,actual)

    def testNumpyAverageOneValueArray(self):
        npsy = NumpySciPy()
        multiArray = [[1,2],[1,2]]
        actual = npsy.numpyAverage(multiArray)
        expected = 1.5
        self.assertEqual(expected,actual)

    def testNumpyAverageOneValueArray(self):
        npsy = NumpySciPy()
        multiArray = [[0.01,0.01],[0.01,0.01]]
        actual = npsy.numpyAverage(multiArray)
        expected = 0.01
        self.assertEqual(expected,actual)

    def testNumpyAverageMixTypesValueArray(self):
        npsy = NumpySciPy()
        multiArray = [[0.01,1],[0.01,1]]
        actual = npsy.numpyAverage(multiArray)
        expected = 0.505
        self.assertEqual(expected,actual)

    def testNumpyAverageOneOffValueArray(self):
        npsy = NumpySciPy()
        multiArray = [[0.01,1],[1,4]]
        actual = npsy.numpyAverage(multiArray)
        expected = 1.5025
        self.assertEqual(expected,actual)

    def testNumpyNPVreturnsNPV(self):
        npsy = NumpySciPy()
        array = [500,600,522]
        actual = npsy.numpyNPV(array,0.01)
        expected = 1605.77
        self.assertEqual(expected,actual)

    def testOneValueArrayNumpyNPVreturnsNPV(self):
        npsy = NumpySciPy()
        array = [500]
        actual = npsy.numpyNPV(array,0.05)
        expected = 500.00
        self.assertEqual(expected,actual)

    def testNumpySTDreturnsSTD(self):
        npsy = NumpySciPy()
        array = [500,500,500]
        actual = npsy.numpySTD(array)
        expected = 0.00
        self.assertEqual(expected,actual)

    def testNumpySTDOneValueArrayreturnsSTD(self):
        npsy = NumpySciPy()
        array = [500]
        actual = npsy.numpySTD(array)
        expected = 0.00
        self.assertEqual(expected,actual)

    def testNumpySTDMultiArrayreturnsSTD(self):
        npsy = NumpySciPy()
        array = [[500,200],[400,600]]
        actual = npsy.numpySTD(array)
        expected = 147.9019945774904
        self.assertEqual(expected,actual)

    def testNumpyCorrelateEmptyArrayreturnsNone(self):
        npsy = NumpySciPy()
        array = []
        actual = npsy.numpyCorrelate(array)
        expected = None
        self.assertEqual(expected,actual)

    def testNumpyCorrelate(self):
        npsy = NumpySciPy()
        array = [[]]
        actual = npsy.numpyCorrelate(array)
        expected = None
        self.assertEqual(expected,actual)

    def testNumpyCorrelate(self):
        npsy = NumpySciPy()
        array = [[1,2,3],[3,4,5]]
        actual = npsy.numpyCorrelate(array)
        expected = np.array([26])
        self.assertEqual(expected,actual)

    def testInitDataFrameReturnsDataFame(self):
        stocksData ={
            "Blackstone":[49.56,50.70,51.18,52.80,52.87],
            "KKR": [24.24,24.60,26.04,26.90,26.66]
        }
        npsy = NumpySciPy()
        actual = npsy.initDataFrame(stocksData)
        print(actual)
        expected = pd.DataFrame(stocksData)
        print(expected)


    def testInitDataFrameReturnsDataFameWithDates(self):
        stocksData ={
            "Blackstone":[49.56,50.70,51.18,52.80,52.87],
            "KKR": [24.24,24.60,26.04,26.90,26.66]
        }
        dates = ['5/4/20','5/5/20','5/6/20','5/8/20','5/9/20']
        npsy = NumpySciPy()
        actual = npsy.initDataFrame(stocksData,rows=dates)
        expected = pd.DataFrame(stocksData,index=dates)

    def testEmptyDataInitDataFrameReturnsDataFame(self):
        stocksData ={
        }
        npsy = NumpySciPy()
        actual = npsy.initDataFrame(stocksData)
        expected = pd.DataFrame(stocksData)

    def testEmptyheadDFReturnsHeadDataFame(self):
        stocksData ={
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData)
        actual = npsy.headDF(df)
        expected = pd.DataFrame(stocksData).head()

    def testEmptyHeadDFReturnsHeadDataFame(self):
        stocksData ={
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData)
        actual = npsy.headDF(df)
        expected = pd.DataFrame(stocksData).head()

    def testHeadDFReturnsHeadDataFame(self):
        stocksData ={
            "Blackstone":[49.56,50.70,51.18,52.80,52.87],
            "KKR": [24.24,24.60,26.04,26.90,26.66]
        }
        dates = ['5/4/20','5/5/20','5/6/20','5/8/20','5/9/20']
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData,rows=dates)
        actual = npsy.headDF(df)
        expected = pd.DataFrame(stocksData,index=dates).head()

    def testEmptyTailDFReturnsTailDataFame(self):
        stocksData ={
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData)
        actual = npsy.tailDF(df)
        expected = pd.DataFrame(stocksData).tail()

    def testTailDFReturnsTailDataFame(self):
        stocksData = {
            "Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87],
            "KKR": [24.24, 24.60, 26.04, 26.90, 26.66]
        }
        dates = ['5/4/20', '5/5/20', '5/6/20', '5/8/20', '5/9/20']
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData, rows=dates)
        actual = npsy.tailDF(df,numOfRows=2)
        expected = pd.DataFrame(stocksData, index=dates).tail(2)


    def testDefaul10TailDFReturnsTailDataFame(self):
        stocksData = {
            "Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87,24.24, 24.60, 26.04, 26.90, 26.66],
            "KKR": [24.24, 24.60, 26.04, 26.90, 26.66,24.24, 24.60, 26.04, 26.90, 26.66]
        }
        dates = ['5/4/20', '5/5/20', '5/6/20', '5/8/20', '5/9/20','5/4/20', '5/5/20', '5/6/20', '5/8/20', '5/9/20']
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData, rows=dates)
        actual = npsy.tailDF(df,)
        expected = pd.DataFrame(stocksData, index=dates).tail(10)

    def testappendDFReturnsEmptyDataFame(self):
        stocksData = {
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData)
        actual = npsy.appendDF(dataframe=df,appendDataFrame=df)
        expected = pd.DataFrame(df).append(df)


    def testappendDFReturnsDataFame(self):
        stocksData = {
            "Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87, 24.24, 24.60, 26.04, 26.90, 26.66],
            "KKR": [24.24, 24.60, 26.04, 26.90, 26.66, 24.24, 24.60, 26.04, 26.90, 26.66]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData)
        actual = npsy.appendDF(dataframe=df,appendDataFrame=df)
        expected = pd.DataFrame(stocksData).append(df)


    def testdropDuplicateDFReturnsEmptyDataFame(self):
        stocksData = {
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stocksData)
        df = npsy.appendDF(dataframe=df,appendDataFrame=df)
        actual = npsy.dropDuplicatesDF(df)
        expected = pd.DataFrame(stocksData).append(df).drop_duplicates()

    def testdropDuplicateReturnsDataFame(self):
        stockData = {
            "Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87, 24.24, 24.60, 49.56, 26.90, 26.66]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        df = npsy.appendDF(dataframe=df,appendDataFrame=df)
        actual = npsy.dropDuplicatesDF(df)
        expected = pd.DataFrame(stockData).append(df).drop_duplicates()

    def testaverageDFReturnsEmptySeriesMean(self):
        stockData ={
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.averageDF(df)
        expected = pd.DataFrame(stockData).mean()

    def testaverageDFReturnsSeriesMean(self):
        stockData ={
            "Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87, 24.24, 24.60, 49.56, 26.90, 26.66]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.averageDF(df)
        expected = pd.DataFrame(stockData).mean()

    def testaverageMultiColumnDFReturnsSeriesMean(self):
        stockData ={
            "Blackstone":[49.56,50.70,51.18,52.80,52.87],
            "KKR": [24.24,24.60,26.04,26.90,26.66]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.averageDF(df)
        expected = pd.DataFrame(stockData).mean()

    def testEmptyDataFrameCountReturnEmptySeries(self):
        stockData = {
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.countDF(df)
        expected = pd.DataFrame(stockData).count()


    def testDataFrameCountReturnSeriesOfCount(self):
        stockData = {
            "Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87],
            "KKR": [24.24, 24.60, 26.04, 26.90, 26.66]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.countDF(df)
        expected = pd.DataFrame(stockData).count()

    def testEmptyArrayInitSeriesreturnEmptySeries(self):
        priceArray = []
        npsy = NumpySciPy()
        actual = npsy.initSeries(priceArray)
        expected = pd.Index(priceArray)

    def testSingleValArrayInitSeriesreturnSerie(self):
        priceArray = [49.56]
        npsy = NumpySciPy()
        actual = npsy.initSeries(priceArray)
        expected = pd.Index(priceArray)

    def testArrayInitSeriesreturnSeries(self):
        priceArray = [49.56, 50.70, 51.18, 52.80, 52.87]
        npsy = NumpySciPy()
        actual = npsy.initSeries(priceArray)
        expected = pd.Index(priceArray)

    def test2DArrayInitSeriesreturnObjectSeries(self):
        priceArray = [[49.56, 50.70, 51.18, 52.80, 52.87],[24.24, 24.60, 26.04, 26.90, 26.66]]
        npsy = NumpySciPy()
        actual = npsy.initSeries(priceArray)
        expected = pd.Index(priceArray)

    def testEmptyArrayvalueCountSeriesreturnEmptySeries(self):
        priceArray = []
        npsy = NumpySciPy()
        series = npsy.initSeries(priceArray)
        actual = npsy.valueCountSeries(series)
        expected = pd.Index(priceArray).value_counts()

    def testSingleValueArrayValueCountSeriesreturnSerie(self):
        priceArray = [52.80]
        npsy = NumpySciPy()
        series = npsy.initSeries(priceArray)
        actual = npsy.valueCountSeries(series)
        expected = pd.Index(priceArray).value_counts()

    def testArrayvalueCountSeriesreturnEmptySeries(self):
        priceArray = [52.80, 52.80, 51.18, 52.80,51.18,52.87]
        npsy = NumpySciPy()
        series = npsy.initSeries(priceArray)
        actual = npsy.valueCountSeries(series)
        expected = pd.Index(priceArray).value_counts()

    def testEmptyDataFrameCorrReturnEmptySeries(self):
        stockData = {
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.countDF(df)
        expected = pd.DataFrame(stockData).corr()

    def testSingleValDictDataFrameCorrReturnSerie(self):
        stockData = {"Blackstone": [49.56]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.countDF(df)
        expected = pd.DataFrame(stockData).corr()

    def testDictDataFrameCorrReturnSerie(self):
        stockData = {"Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87]
        }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.countDF(df)
        expected = pd.DataFrame(stockData).corr()

    def testDualArrayDictDataFrameCorrReturnSeries(self):
        stockData = {"Blackstone": [49.56, 50.70, 51.18, 52.80, 52.87],
                     "KKR": [24.24, 24.60, 26.04, 26.90, 26.66]
                     }
        npsy = NumpySciPy()
        df = npsy.initDataFrame(stockData)
        actual = npsy.countDF(df)
        expected = pd.DataFrame(stockData).corr()
        print(actual)
        print(expected)