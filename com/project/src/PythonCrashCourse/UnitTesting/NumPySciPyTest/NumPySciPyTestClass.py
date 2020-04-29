import unittest
from com.project.src.PythonCrashCourse.DataScience.NumPySciPy import NumpySciPy

class NumpySciPyTestClass(unittest.TestCase):

    def test_numpyArray_returns_unit(self):
        npsp = NumpySciPy()
        arrays = [[1,2,3],[3,4,6]]
        npsp.numpyArray(arrays)