import unittest
from com.project.src.FlaskApp.src.TickerCLS import ListTicker

class ListTickerTest(unittest.TestCase):

    def test_getTickersPermittedExpectedEmptyList(self):
        stringList = []
        lt = ListTicker(tickersPermitted=stringList)
        actual = lt.getTickersPermitted()
        expected = []
        self.assertEqual(actual,expected)

    def test_getTickersNotPermittedExpectedEmptyList(self):
        stringList = []
        lt = ListTicker(tickersNotPermitted=stringList)
        actual = lt.getTickersNotPermitted()
        expected = []
        self.assertEqual(actual,expected)