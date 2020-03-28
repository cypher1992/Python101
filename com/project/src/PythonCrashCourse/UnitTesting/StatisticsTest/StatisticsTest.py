import unittest
# from path of file import class
from com.project.src.PythonCrashCourse.DataScience.Statistics import Statistics

class StatisticsTest(unittest.TestCase):

    def test_getListOfVals_returns_List(self):
        listOfVals = [0,2,4,6,8,10]
        stats = Statistics(listOfVals)
        actual = stats.getListOfVals()
        expected = [0,2,4,6,8,10]
        self.assertEqual(actual,expected)