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

    def test_rangeList_return_none(self):
        emptyList = []
        stat = Statistics(emptyList)
        actual = stat.rangeList()
        expected = None
        self.assertEqual(actual,expected)

    def test_rangeList_return_range(self):
        listOfVal = [1,2,3,4,5]
        stat = Statistics(listOfVal)
        actual = stat.rangeList()
        expected = 4
        self.assertEqual(actual,expected)

    def test_medianEmtpyList_return_none(self):
        emptyList = []
        stat = Statistics(emptyList)
        actual = stat.median()
        expected = None
        self.assertEqual(expected,actual)

    def test_medianOddList_return_3(self):
        oddList = [1, 2, 3, 4, 5]
        stat = Statistics(oddList)
        actual = stat.median()
        expected = 3
        self.assertEqual(expected, actual)

    def test_medianEvenList_return_2_5(self):
        evenList = [1, 2, 3, 4]
        stat = Statistics(evenList)
        actual = stat.median()
        expected = 2.5
        self.assertEqual(expected, actual)

    def test_negativeMin_rangeList_return_range(self):
        listOfVal = [-1, 2, 3, 4, 5]
        stat = Statistics(listOfVal)
        actual = stat.rangeList()
        expected = 6
        self.assertEqual(actual, expected)

    def test_negativeMinMax_rangeList_return_range(self):
        listOfVal = [-1, -2, -3, -4, -5]
        stat = Statistics(listOfVal)
        actual = stat.rangeList()
        expected = 4
        self.assertEqual(actual, expected)

    def test__rangeListsameInterval_return_range(self):
        listOfVal = [1, 1, 1]
        stat = Statistics(listOfVal)
        actual = stat.rangeList()
        expected = 0
        self.assertEqual(actual, expected)

    def test_arthmeticMean_return_3(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.arithmeticMean()
        expected = 3
        self.assertEqual(actual,expected)

    def test_arithmeticMean_return_0(self):
        list = []
        stat = Statistics(list)
        actual = stat.arithmeticMean()
        expected = 0
        self.assertEqual(actual,expected)

    def test_arithmeticMean_return_1(self):
        list = [1,1,1]
        stat = Statistics(list)
        actual = stat.arithmeticMean()
        expected = 1
        self.assertEqual(actual,expected)

    def test_geometricMean_return_0(self):
        list = []
        stat = Statistics(list)
        actual = stat.geometricMean()
        expected = 0
        self.assertEqual(actual,expected)

    def test_geometricMean_return_2_60(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.geometricMean()
        expected = 2.605171084697352
        self.assertEqual(actual,expected)

    def test_geometricMeanSameValue_return_1(self):
        list = [1,1,1]
        stat = Statistics(list)
        actual = stat.geometricMean()
        expected = 1
        self.assertEqual(actual,expected)

    def test_harmonicMean_return_none(self):
        emptyList = []
        stat = Statistics(emptyList)
        actual = stat.harmonicMean()
        expected = None
        self.assertEqual(actual,expected)

    def test_harmonicMean_0value_return_None(self):
        zerolist = [0,21,414]
        stat = Statistics(zerolist)
        actual = stat.harmonicMean()
        expected = None
        self.assertEqual(actual, expected)

    def test_harmonicMean_0value_return_2(self):
        zerolist = [1,4,4]
        stat = Statistics(zerolist)
        actual = stat.harmonicMean()
        expected = 2
        self.assertEqual(actual, expected)

    def test_harmonicMean_sameValue_return_1(self):
        zerolist = [1, 1, 1]
        stat = Statistics(zerolist)
        actual = stat.harmonicMean()
        expected =1
        self.assertEqual(actual, expected)

    def test_mode_return_2(self):
        statlist = [2,4,2,6,2,7,8,2,7,3,20,3]
        stat = Statistics(statlist)
        actual = stat.mode()
        expected = 2
        self.assertEqual(expected,actual)

    def test_mode_returns_none(self):
        emptyList = []
        stat = Statistics(emptyList)
        actual = stat.mode()
        expected = None
        self.assertEqual(expected,actual)

    def testMeanAbsoluteDeviation_returns_None(self):
        emptylist = []
        stat = Statistics(emptylist)
        actual = stat.meanAbsoluteDeviation()
        expected = None
        self.assertEqual(expected,actual)

# need to test mad

    def testvariance_returns_none(self):
        emptyList=[]
        stat = Statistics(emptyList)
        actual = stat.variance()
        expected = None
        self.assertEqual(expected,actual)

    def testvariance_returns_populationVariance(self):
        popList = [1,2,3,4,5]
        stat = Statistics(popList)
        actual = stat.variance()
        expected = 2
        self.assertEqual(actual,expected)