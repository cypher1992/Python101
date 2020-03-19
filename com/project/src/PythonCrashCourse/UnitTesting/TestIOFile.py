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

    def test_readDelimterByLine_returns_LengthOf6(self, path=path):
        """io.readDelimterByLine() expected 'ListOfLine'"""
        iof = IOFile
        path += 'delimitRead.txt'
        actual = iof.readDelimterByLine(iof, path, ',')
        actual = len(actual)
        expected = 5
        self.assertEqual(actual, expected)

    def test_writeToFileDelimter_returns_LengthOf1(self, path=path):
        iof = IOFile
        path += 'delimitWrite.txt'
        iof.writeToFileDelimiter(iof, path, 'Goldman Sacs', 'GS', ',')
        actual = iof.readDelimterByLine(iof, path, ',')
        actual = len(actual)
        expected = 1
        self.assertEqual(actual, expected)

    def test_appendToFileDelimter_returnsAddToExistingFile(self,path = path):
        iof = IOFile
        path += 'delimitAppend.txt'
        iof.writeToFileDelimiter(iof,path,'','','')
        iof.appendToFileDelimiter(iof,path,'Goldman Sacs','GS',',')
        iof.appendToFileDelimiter(iof, path, 'Blackstone', 'BX', ',')
        actual = iof.readDelimterByLine(iof, path , ',')
        actual = len(actual)
        expected = 2
        self.assertEqual(actual,expected)

    def test_deleteContentFile_returns0lines(self,path = path):
        iof = IOFile
        path += 'delimitDelete.txt'
        iof.appendToFileDelimiter(iof, path, 'Goldman Sacs', 'GS', ',')
        iof.appendToFileDelimiter(iof, path, 'Blackstone', 'BX', ',')
        actual = iof.readDelimterByLine(iof,path,',')
        actual = len(actual)
        iof.deleteContentFile(iof,path)
        expected = iof.readDelimterByLine(iof, path, ',')
        expected = len(expected)
        self.assertEqual(actual-2,expected)



