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

    def test_findPatternOfNotADigitmatchPatternsTelephoneReturnsTrue(self):
        string = "7-917-293-191"
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"\D")
        patternX = re.compile(r'\D')
        expected = []
        print(actual)
        #Using \D searches for all characters that is not between 0 - 9
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_findPatternOfDotmatchPatternsWebsiteReturnsTrue(self):
        string = "www.amandaplease.com"
        reg = Regex(string)
        actual = reg.matchPatterns(pattern=r"\.")
        patternX = re.compile(r'\.')
        expected = []
        #Backslash for metacharacters are need due to regex . ^ $ * + ? { } [ ] \ | ( )
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        self.assertEqual(actual,expected)

    def test_findPatternOfDotExpressionmatchPatternsWebsiteReturnsTrue(self):
        string = "www.amandaplease.com"
        reg = Regex(string)
        regexExpression = r"."
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # . return all characters that are not a new line
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual,expected)

    def test_findPatternOfwordExpressionmatchPatternsWebsiteReturnsTrue(self):
        string = "www.amandaplease.com"
        reg = Regex(string)
        regexExpression = r"\w"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \w returns a-z A-Z 0-9 _
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual,expected)

    def test_findPatternOfNotWordExpressionMatchPatternsWebsite(self):
        string = "www.amandaplease.com"
        reg = Regex(string)
        regexExpression = r"\W"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \W  returns not a-z A-Z 0-9 _ there should only return .
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual,expected)

    def test_findPatternOfWhiteSpaceExpressionMatchPatternsString(self):
        string = """I said I like it like that
                
        """
        reg = Regex(string)
        regexExpression = r"\s"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \s - return whitespac(space,tab, and newline)
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual,expected)

    def test_findPatternOfNotWhiteSpaceExpressionMatchPatternsString(self):
        string = """I said I like it like that

        """
        reg = Regex(string)
        regexExpression = r"\S"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \s - return whitespac(space,tab, and newline)
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_findPatternOfBoundaryExpressionMatchPatternsString(self):
        string = """I said I like it like that

        """
        reg = Regex(string)
        regexExpression = r"\bsaid\b"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \b - return boundary between words
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_findPatternOfNotBoundaryExpressionMatchPatternsHA(self):
        string = """Ha HaHa

        """
        reg = Regex(string)
        regexExpression = r"\BHa"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \B - return not word boundary
        # match the last ha
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_findPatternOfWordBoundaryExpressionMatchPatternsHA(self):
        string = """Ha HaHa

        """
        reg = Regex(string)
        regexExpression = r"\bHa"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # \b - return  word boundary
        # match the begin with boundary than ha
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_findPatternOfStartofStringMatchPatternsString(self):
        string = """I said I like it like that

        """
        reg = Regex(string)
        regexExpression = r"^I"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # ^ start of a string
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_matchPatternsStartOfSaidReturnsNothing(self):
        string = """I said I like it like that

        """
        reg = Regex(string)
        regexExpression = r"^said"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # ^ start of a string
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_matchPatternsThatAtEndReturnsInstance(self):
        string = """I said I like it like that"""
        reg = Regex(string)
        regexExpression = r"that$"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # $ end of a string
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_matchPatternsLikeAtEndReturnsNothing(self):
        string = """I said I like it like that"""
        reg = Regex(string)
        regexExpression = r"like$"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # $ end of a string
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_matchPatternstelephoneEndReturnsInstanceWithHyphen(self):
        string = """917-293-9422
        514*264*8577"""
        reg = Regex(string)
        regexExpression = r"\d\d\d-\d\d\d-\d\d\d\d"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # /d - for digits
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_matchPatternstelephoneEndReturnsAllInstance(self):
        string = """917-293-9422
        514*264*8577"""
        reg = Regex(string)
        regexExpression = r"\d\d\d.\d\d\d.\d\d\d\d"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # /d - for digits - . all instance of word
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_PeriodIsNotTheBestOptmatchPatternstelephoneEndReturnsAllInstance(self):
        string = """
        917-293-9422
        514*264*8577
        516a524a7485
        516452487485
        """
        reg = Regex(string)
        regexExpression = r"\d\d\d.\d\d\d.\d\d\d\d"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # /d - for digits
        # . all instance of word
        # period is not the best instance because it returns also alphaNumeric instance
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_SetSelectormatchPatternstelephoneEndReturnsAllInstance(self):
        string = """
        917-293-9422
        514*264*8577
        516a524a7485
        516452487485
        """
        reg = Regex(string)
        regexExpression = r"\d\d\d[-*]\d\d\d[-*]\d\d\d\d"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # /d - for digits
        # . all instance of word
        # [-*] set selector looking for only instances of - and * in that one char
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)

    def test_matchPatterns917telephoneEndReturnsAllInstance(self):
        string = """
           917-293-9422
           514*264*8577
           516a524a7485
           516452487485
           917-124-1173
           """
        reg = Regex(string)
        regexExpression = r"[9][1][7][-*]\d\d\d[-*]\d\d\d\d"
        actual = reg.matchPatterns(pattern=regexExpression)
        patternX = re.compile(regexExpression)
        expected = []
        # /d - for digits
        # . all instance of word
        # [-*] set selector looking for only instances of - and * in that one char
        for match in patternX.finditer(string):
            expected.append(match.start())
            expected.append(match.group())
        print(actual)
        self.assertEqual(actual, expected)