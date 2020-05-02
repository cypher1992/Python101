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
