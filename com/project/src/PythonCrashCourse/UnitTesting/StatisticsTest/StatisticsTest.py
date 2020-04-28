import unittest
import random
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

    def testmeanabsolutedeviation_returns_None(self):
        emptylist = []
        stat = Statistics(emptylist)
        actual = stat.meanAbsoluteDeviation()
        expected = None
        self.assertEqual(expected,actual)

    def testmeanabsolutedeviation_returns_None(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.meanAbsoluteDeviation()
        expected = 1.2
        self.assertEqual(expected,actual)

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

    def testvariance_return_sampleVariance(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.variance(population = False)
        expected = 2.5
        self.assertEqual(expected,actual)

    def teststandarddeviation_returns_none(self):
        emptylist = []
        stat = Statistics(emptylist)
        actual = stat.standardDeviation()
        expected = None
        self.assertEqual(expected,actual)

    def testpopulationstandarddeviation_returns_std(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.standardDeviation()
        expected = 1.4142135623730951
        self.assertEqual(expected,actual)

    def testsamplestandarddeviation_returns_std(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.standardDeviation(population=False)
        expected = 1.5811388300841898
        self.assertEqual(actual,expected)

    def testChebyshevInequalityreturnNone(self):
        emptyList = []
        stat = Statistics(emptyList)
        actual = stat.chebyshevInequality()
        expected = None
        self.assertEqual(expected,actual)

    def testChebyshevInequalityreturnCI(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.chebyshevInequality()
        expected = 0.5000000000000001
        self.assertEqual(expected,actual)

    def testPlotDataReturnEmptyGraph(self):
        emptyList =[]
        stat = Statistics(emptyList)
        stat.plotData()

    def testPlotDataReturnGraph(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        stat.plotData()

    def testPlotDataLargeDataSetReturnGraph(self):
        list = []
        for i in range(0,99):
            list.append(random.randint(0,99))
        stat = Statistics(list)
        stat.plotData()

    def testPlotDataMeanEmptyDataSetReturnGraph(self):
        emptylist = []
        stat = Statistics(emptylist)
        stat.plotDataMean()

    def testPlotDataMeanLargeDataSetReturnGraph(self):
        list = []
        for i in range(0,99):
            list.append(random.randint(0,99))
        stat = Statistics(list)
        stat.plotDataMean()

    def testZScoreEmptyListReturnNone(self):
        emptylist = []
        stat = Statistics(emptylist)
        actual = stat.zscore()
        expected = None
        self.assertEqual(expected,actual)

    def testZScoreOneValuelistReturnList(self):
        list = [1]
        stat = Statistics(list)
        actual = stat.zscore()
        expected = {1:0}
        self.assertEqual(expected,actual)

    def testZScorelistReturnList(self):
        list = [1,2,3,4,5]
        stat = Statistics(list)
        actual = stat.zscore()
        expected = {1:-1.414213562373095, 2:-0.7071067811865475, 3:0.0, 4:0.7071067811865475, 5:1.414213562373095}
        self.assertEqual(expected,actual)

    def testZScoreSameValuelistReturnList(self):
        list = [1,1,1,1,1]
        stat = Statistics(list)
        actual = stat.zscore()
        expected = None
        self.assertEqual(expected,actual)

    def testcorrelationCoefficientReturnsNone(self):
        emptyList =[]
        stat = Statistics(emptyList)
        expected = None
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)

    def testcorrelationCoefficientReturnsZero(self):
        list =[1]
        stat = Statistics(list)
        expected = 0
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)

    # correlation needs to stay between -1 to 1
    def testcorrelationCoefficientReturnsRvalue(self):
        list =[1,2,3,4,5]
        stat = Statistics(list)
        expected = 0.9999999999999998
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)

    def testnegativeCorrelationCoefficientReturnsRvalue(self):
        list =[-1,-2,-3,-4,-5]
        stat = Statistics(list)
        expected = -0.9999999999999998
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)

    def testsameDataSetCorrelationCoefficientReturnsRvalue(self):
        list =[1,1,1,1,1]
        stat = Statistics(list)
        expected = 0
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)

    def testsameDataSetCorrelationCoefficientReturnsRvalue(self):
        list =[1,2,1,2,1]
        stat = Statistics(list)
        expected = 0
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)

    def testoneOffCorrelationCoefficientReturnsRvalue(self):
        list =[1,2,1,2,5]
        stat = Statistics(list)
        expected = 0.7698003589195009
        actual = stat.correlationCoefficient()
        self.assertEqual(expected,actual)