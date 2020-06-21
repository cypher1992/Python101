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

