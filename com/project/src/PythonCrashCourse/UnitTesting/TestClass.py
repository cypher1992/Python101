# Uniting testing with unittest
# unit test - verifies that specific part of function behavior works
# test case - is a collection of unit test that together proves that a function behaves as suppoised
# Good Test Case - considers all possibilities of input
# full coverage - includes a full range of unit tests covering all possible ways to use function

import unittest
from com.project.src.PythonCrashCourse.ClassStructure.Stock import Stock


class StockTest(unittest.TestCase):
        """Test Case for Stock.py"""
        # setup
        def test_getTicker_returns_BX(self):
            """bx.getTicker() expected 'BX'"""
            bx = Stock("BlackStone", "BX", 36.44, "3/7/20")
            tickerName = bx.getTicker()
            expected = "BX"
            self.assertEqual(tickerName,expected)

        def test_getCompany_returns_Blackstone(self):
            """bx.getCompany() excepted Blackstone"""
            bx = Stock("BlackStone", "BX", 36.44, "3/7/20")
            actual = bx.getCompany()
            expected = "BlackStone"
            self.assertEqual(actual,expected)



def main():
    if __name__ == '__main__':
        unittest.main()

main()