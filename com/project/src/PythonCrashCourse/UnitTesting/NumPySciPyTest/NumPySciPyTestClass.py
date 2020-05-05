import unittest
import numpy as np
import scipy as sp
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

    def testNumpyAverageOneValueArray(self):
        npsy = NumpySciPy()
        multiArray = [[0.01,1],[0.01,1]]
        actual = npsy.numpyAverage(multiArray)
        expected = 0.505
        self.assertEqual(expected,actual)