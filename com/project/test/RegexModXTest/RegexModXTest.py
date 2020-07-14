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

    def test_matchPatternsAlphabetreturnsTrue(self):
        string = "abcAbcABCNYCBCAabc"
        reg = Regex(string)
        actual = reg.matchPatterns()
        patternX = re.compile(r'abc')
        expected = []
        for match in patternX.finditer(string):
            #match.start() = starting position of pattern
            expected.append(match.start())
            #match.group() = returns result of the first instance of match
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_matchPatternsTelephoneReturnsTrue(self):
        string = "1-917-293-9174"
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"917")
        patternX = re.compile(r'917')
        expected = []
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_matchPatternsRotateTelephoneReturnsTrue(self):
        string = "7-917-293-191"
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"917")
        patternX = re.compile(r'917')
        expected = []
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_blockStringmatchsRotateTelephoneReturnsPositionAndInstanceOfMatch(self):
        string = """7-917-293-1191
        7"""
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"917")
        patternX = re.compile(r'917')
        expected = []
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_BlockStringEntermatchPatternReturnsPositionAndInstanceOfMatch(self):
        string = """7-917-293-1191
        917"""
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"917")
        patternX = re.compile(r'917')
        expected = []
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_pureMatchPatternsAlphabetreturns2(self):
        string = "abcAbcABCNYCBCAabc"
        reg = Regex(string)
        actual = reg.pureMatchPatterns()
        patternX = re.compile(r'abc')
        expected = 2
        self.assertEqual(len(actual), expected)

    def test_findPatternOfDigitmatchPatternsTelephoneReturnsTrue(self):
        string = "7-917-293-191"
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"\d")
        patternX = re.compile(r'\d')
        expected = []
        #Using \d searches for all characters that is between 0 - 9
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)