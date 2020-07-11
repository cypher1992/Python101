import re
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

    def test_isAllLettersreturnsTrue(self):
        string = "HelloWorld"
        reg = Regex(string)
        actual = reg.isAllLetters()
        expected = True
        self.assertEqual(actual,expected)

    def test_emptyStringisAllLettersreturnsFalse(self):
        string = ""
        reg = Regex(string)
        actual = reg.isAllLetters()
        expected = False
        self.assertEqual(actual,expected)

    def test_NumericStringisAllLettersreturnsFalse(self):
        string = "1231414"
        reg = Regex(string)
        actual = reg.isAllLetters()
        expected = False
        self.assertEqual(actual,expected)

    def test_NumericWithAlphaStringisAllLettersreturnsFalse(self):
        string = "123ABC"
        reg = Regex(string)
        actual = reg.isAllLetters(pattern = "^[a-zA-Z]+$")
        expected = False
        self.assertEqual(actual,expected)

    def test_NumericStringisAllLettersreturnsFalse(self):
        string = "123"
        reg = Regex(string)
        actual = reg.isAllLetters(pattern = "^[0-9]+$")
        expected = True
        self.assertEqual(actual,expected)

    def test_isPatternOfreturnsTrue(self):
        string = "HelloWorld"
        reg = Regex(string)
        actual = reg.isPatternOf()
        expected = True
        self.assertEqual(actual,expected)

    def test_isPatternOfOnlyLetterOfreturnsTrue(self):
        string = "HelloWorld"
        pattern = "^[a-zA-Z]+$"
        reg = Regex(string)
        actual = reg.isPatternOf(pattern=pattern)
        expected = True
        self.assertEqual(actual, expected)

    def test_isPatternOfOnlyDigitsOfreturnsTrue(self):
        string = "123"
        pattern = "^[0-9]+$"
        reg = Regex(string)
        actual = reg.isPatternOf(pattern=pattern)
        expected = True
        self.assertEqual(actual, expected)

    def test_isPatternOfOnlyDigitsOfreturnsTrue(self):
        string = "917-293-9535"
        pattern = '^\d\d\d-\d\d\d-\d\d\d\d$'
        reg = Regex(string)
        actual = reg.isPatternOf(pattern=pattern)
        expected = True
        self.assertEqual(actual, expected)

# not working!!!!
    def test_matchPatternsDigitreturnsTrue(self):
        string = "917-293-9535"
        pattern = r'\d'
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=pattern)
        patternX = re.compile(pattern)
        expected = patternX.finditer(string)
        self.assertEqual(actual,expected)