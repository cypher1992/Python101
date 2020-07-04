import unittest
from com.project.src.PythonCrashCourse.RegexPack.RegexModX import Regex

class RegExModCase(unittest.TestCase):

    def test_isInstanceOfRegexModX(self):
        string = "HW"
        regex = Regex(string)
        self.assertTrue(isinstance(regex,Regex))
