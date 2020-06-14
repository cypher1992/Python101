import unittest
from com.project.src.PythonCrashCourse.DataStructure.ListStructure import List

class ListTest(unittest.TestCase):

    def test_getListreturnsList(self):
        listChars = ['C','B','A']
        listObj = List(list = listChars)
        actual = listObj.getList()
        expected = listChars
        self.assertEqual(expected,actual)

    def test_setListreturnsList(self):
        emptylist = []
        listObj = List(list = emptylist)
        listChars = ['C','B','A']
        listObj.setList(listChars)
        actual = listObj.getList()
        expected = listChars
        self.assertEqual(expected,actual)

    def test_appendToListreturnsList(self):
        emptylist = []
        listObj = List(list = emptylist)
        listChars = ['C']
        listObj.appendToList('C')
        actual = listObj.getList()
        expected = listChars
        self.assertEqual(expected,actual)
