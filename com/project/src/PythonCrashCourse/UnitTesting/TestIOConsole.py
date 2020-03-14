import unittest
from com.project.src.PythonCrashCourse.IOPuts.IOConsole import IOConsole


class IOConsoleTest(unittest.TestCase):
    def test_takeInput_returns_Zero_Mustafa(self):
        """io.i() expected 'Zero Mustafa'"""
        io = IOConsole
        actual = io.takeInput("Get Name: ")
        expected = "Zero Mustafa"
        self.assertEqual(actual, expected)