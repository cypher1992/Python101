import unittest
# from path of file import class
from com.project.src.PythonCrashCourse.DataScience.Statistics import Statistics

class StatisticsTest(unittest.TestCase):

    def test_getListOfVals_returns_List(self):
        listOfVals = [0,2,4,6,8,10]
        stats = Statistics(listOfVals)
        actual = stats.getList()
        expected = [0,2,4,6,8,10]
        self.assertEqual(actual,expected)

    def test_setListOfVals_return_None(self):
        listOfVals = [0, 2, 4, 6, 8, 10]
        newList =  [1,3,5,7,9]
        stats = Statistics(listOfVals)
        stats.setListOfVals(newList)
        actual = stats.getList()
        expected = [1,3,5,7,9]
        self.assertEqual(actual,expected)

    def test_arthmeticMean_return_(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.arithmeticMean()
        expected = 3
        self.assertEqual(actual,expected)

