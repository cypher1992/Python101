import unittest
from com.project.src.PythonCrashCourse.ErrorHandling.TryAndCatchErrors import ListClass

class TryAndCatchTest(unittest.TestCase):

    def test_getList_returns_List(self):
        lst = [1,2,3,4]
        tace = ListClass(lst)
        actual = tace.getList()
        expected = [1,2,3,4]
        self.assertEqual(actual,expected)

    def test_setList_returns_newList(self):
        lst = [1,2,3,4]
        newList = [4,3,2,1]
        tace = ListClass(lst)
        tace.setList(newList)
        actual = tace.getList()
        expected = [4,3,2,1]
        self.assertEqual(actual,expected)

    def test_findValue_returns_value(self):
        lst = [1,2,3,4]
        tace = ListClass(lst)
        actual = tace.findValue(2)
        expect = 2
        self.assertEqual(actual,expect)

    def test_findValue_returns_error(self):
        lst = [1, 2, 3, 4 ]
        tace = ListClass(lst)
        actual = tace.findValue(1100)
        expect = None
        self.assertEqual(actual,expect)