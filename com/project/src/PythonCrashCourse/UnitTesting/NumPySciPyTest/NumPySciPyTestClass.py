import unittest
import numpy as np
import scipy as sp
from com.project.src.PythonCrashCourse.DataScience.NumPySciPy import NumpySciPy


class NumpySciPyTestClass(unittest.TestCase):

    def test_numpyArray_returns_unit(self):
        npsp = NumpySciPy()
        arrays = [[1,2,3],[3,4,6]]
        actual = npsp.numpyArray(arrays)
        expected = np.array(arrays)
        boolArray= actual == expected
        isTrue =None
        if False in boolArray:
            isTrue = False
        else:
            isTrue = False
        self.assertTrue(isTrue)