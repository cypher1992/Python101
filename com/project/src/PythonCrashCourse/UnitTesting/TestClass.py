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

        def test_getPrice_return_36dot44(self):
            "bx.getPrice() expected 36.44"
            bx = Stock("BlackStone", "BX", 36.44, "3/7/20")
            actual = bx.getPrice()
            expected = 36.44
            self.assertEqual(actual,expected)

        def test_getDate_return_3720(self):
            "bx.getDate() expected 3/7/20"
            bx = Stock("BlackStone","BX",36.44,"3/7/20")
            actual = bx.getDate()
            expected = "3/7/20"
            self.assertEqual(actual,expected)

        def test_getId_return_1(self):
            "bx.getID() expected 1"
            bx = Stock("BlackStone","BX",36.44,"3/7/20")
            actual =bx.getID()
            expected = 1
            self.assertEqual(actual,expected)

        def test_setCompany_return_Citi_Corp(self):
            "c.setCompany() expected 'Citi Corp'"
            c = Stock("Citi", "C", 22.44, "3/7/20")
            c.setCompany("Citi Corp")
            actual = c.getCompany()
            expected = "Citi Corp"
            self.assertEqual(actual, expected)

        def test_setTicker_return_CT(self):
            "c.setTicker() expected 'CT'"
            c = Stock("Citi", "C", 22.44, "3/7/20")
            c.setTicker("CT")
            actual = c.getTicker()
            expected = "CT"
            self.assertEqual(actual, expected)

        def test_updatePriceWithDate_return_priceDate(self):
            "c.updatePriceWithDate() expected '25.66, 3/10/20"
            c = Stock("Citi", "C", 22.44, "3/7/20")
            c.updatePriceWithDate(25.66,"3/10/20")
            actualPrice = c.getPrice()
            expectedPrice = 25.66
            actualDate = c.getDate()
            expectedDate = "3/10/20"
            self.assertEqual(actualPrice, expectedPrice)
            self.assertEqual(actualDate, expectedDate)

        def test_toString_return_str(self):
            "c.toString() expected 'Stock Class: Citi, C, 22.44, 3/7/20"
            c = Stock("Citi", "C", 22.44, "3/7/20")
            actual = c.toString()
            expected = "Stock Class: Citi, C, 22.44, 3/7/20"
            self.assertEqual(actual, expected)


def main():
    if __name__ == '__main__':
        unittest.main()

main()