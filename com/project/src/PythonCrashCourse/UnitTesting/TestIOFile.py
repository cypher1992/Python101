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