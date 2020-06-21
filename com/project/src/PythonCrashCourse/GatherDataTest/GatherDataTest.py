import unittest
from com.project.src.Experimentation.GatherDataWithThreads.GatherData import GatherData

class MyTestCase(unittest.TestCase):

    def test_gatherdata1_returns_list(self):
        gd = GatherData()
        actual = gd.getDataSource1()
        expected = []
        for i in range(1000000):
            expected.append(i)
        self.assertEqual(actual, expected)

    def test_gatherdata2_returns_list(self):
        gd = GatherData()
        actual = gd.getDataSource2()
        expected = []
        for i in range(100, 1000, 2):
            expected.append(i)
        self.assertEqual(actual, expected)

    def test_gatherdata3_returns_list(self):
        gd = GatherData()
        actual = gd.getDataSource3()
        expected = []
        for i in range(10000000, 20000000, 2500):
            expected.append(i)
        self.assertEqual(actual, expected)