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

    def test_removeValuereturnsList(self):
        list = ['C','B','A']
        listObj = List(list = list)
        listChars = ['C','A']
        listObj.removeValue('B')
        actual = listObj.getList()
        expected = listChars
        self.assertEqual(expected,actual)

    def test_removeValueNonExistantValuereturnsList(self):
        list = ['C','B','A']
        listObj = List(list = list)
        listChars = ['C','B','A']
        try:
            listObj.removeValue('D')
        except(ValueError):
            actual = listObj.getList()
            expected = listChars
            self.assertEqual(expected,actual)

    def test_containValuereturnsBoolean(self):
        emptylist = []
        listObj = List(list = emptylist)
        actual = listObj.containValue('C')
        expected = False
        self.assertEqual(expected,actual)

    def test_sliceListreturnsList(self):
        list = ['C','B','A']
        listObj = List(list = list)
        actual = listObj.sliceList(0,1)
        expected = ['C','B']
        self.assertEqual(expected,actual)

    def test_sliceListreturnUpperBoundList(self):
        list = ['C','B','A']
        listObj = List(list = list)
        actual = listObj.sliceList(2,3)
        expected = ['A']
        self.assertEqual(expected,actual)

    def test_sliceListreturnLowerBoundList(self):
        list = ['C', 'B', 'A']
        listObj = List(list=list)
        actual = listObj.sliceList(-1,0)
        expected = []
        self.assertEqual(expected, actual)

    def test_sliceListreturnNone(self):
        list = ['C', 'B', 'A']
        listObj = List(list=list)
        actual = listObj.sliceList(999,1000)
        expected = None
        self.assertEqual(expected, actual)

    def test_updateToList52returnListReplaced5TO2(self):
        list = [4,3,7,5,6,2,2,1]
        listObj = List(list=list)
        actual = listObj.updateToList(5,2)
        expected = [4,3,7,6,2,2,1,2]
        self.assertEqual(expected, actual)