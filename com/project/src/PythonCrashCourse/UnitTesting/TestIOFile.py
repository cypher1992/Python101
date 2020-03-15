import unittest
from com.project.src.PythonCrashCourse.IOPuts.IOFile import IOFile


class IOFileTest(unittest.TestCase):
    path = 'C:\\Users\\Zero\PycharmProjects\\Python101\\com\\project\\src\\PythonCrashCourse\\IOPuts\\Resource\\'

    def test_readFileByLine_returns_ListOfLines(self,path = path):
        """io.readFile() expected 'ListOfLine'"""
        iof = IOFile
        path += 'textfile.txt'
        actual = iof.readFileByLine(path)
        actual= len(actual)
        expected = 3
        self.assertEqual(actual, expected)

    def test_readDelimterByLine_returns_ListOfLines(self, path=path):
        """io.readDelimterByLine() expected 'ListOfLine'"""
        iof = IOFile
        path += 'delimit.txt'
        actual = iof.readDelimterByLine(iof,path,',')
        actual = len(actual)
        expected = 5
        self.assertEqual(actual, expected)