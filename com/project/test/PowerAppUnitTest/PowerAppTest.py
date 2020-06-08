import unittest
from com.project.src.Project.PowerApp.Power import Power
class PowerAppTest(unittest.TestCase):

    def test_InstanceOfPower(self):
        power = Power()
        isPowerClass = isinstance(power,Power)
        print(isPowerClass)
        self.assertTrue(isPowerClass)

