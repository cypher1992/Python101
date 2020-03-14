import unittest
from com.project.src.PythonCrashCourse.IOPuts.IOFile import IOFile


class IOFileTest(unittest.TestCase):
    def test_readFileByLine_returns_ListOfLines(self):
        """io.readFile() expected 'ListOfLine'"""
        iof = IOFile
        actual = iof.readFileByLine("C:\\Users\\Zero\\Desktop\\textfile.txt")
        actual= len(actual)
        expected = 3
        self.assertEqual(actual, expected)