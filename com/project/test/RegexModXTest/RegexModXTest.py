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
        expected = "HelloWorld"
        regex.setString(expected)
        actual = regex.getString()
        self.assertEqual(actual,expected)

    def test_findLettersreturnsTrue(self):
        string = "HelloWorld"
        reg = Regex(string)
        actual = reg.findLetters()
        expected = True
        self.assertEqual(actual,expected)

    def test_emptyStringfindLettersreturnsFalse(self):
        string = ""
        reg = Regex(string)
        actual = reg.findLetters()
        expected = False
        self.assertEqual(actual,expected)

    def test_NumericStringfindLettersreturnsFalse(self):
        string = "1231414"
        reg = Regex(string)
        actual = reg.findLetters()
        expected = False
        self.assertEqual(actual,expected)

    def test_NumericWithAlphaStringfindLettersreturnsFalse(self):
        string = "123ABC"
        reg = Regex(string)
        actual = reg.findLetters(pattern = "^[a-zA-Z]+$")
        expected = False
        self.assertEqual(actual,expected)


