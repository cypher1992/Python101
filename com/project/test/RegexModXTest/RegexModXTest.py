import unittest
from com.project.src.PythonCrashCourse.RegexPack.RegexModX import Regex

class RegExModCase(unittest.TestCase):

    def test_isInstanceOfRegexModXisTrue(self):
        string = "HW"
        regex = Regex(string)
        self.assertTrue(isinstance(regex,Regex))

    def test_getString(self):
        string = "HW"
        regex = Regex(string)
        actual = regex.getString()
        expected = string
        self.assertEqual(actual,expected)

    def test_setString(self):
        string = "HW"
        regex = Regex(string)
        expected = "HellowWorld"
        regex.setString(expected)
        actual = regex.getString()
        self.assertEqual(actual,expected)

    def test_findLettersreturnsTrue(self):
        string = "HellowWorld"
        reg = Regex(string)
        actual = reg.findLetters()
        expected = True
        self.assertEqual(actual,expected)