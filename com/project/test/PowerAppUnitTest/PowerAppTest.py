import unittest
import psutil
from com.project.src.Project.PowerApp.Power import Power
class PowerAppTest(unittest.TestCase):

    def test_InstanceOfPower(self):
        power = Power()
        isPowerClass = isinstance(power,Power)
        print(isPowerClass)
        self.assertTrue(isPowerClass)

    def test_getBatteryReturnsBatteryStats(self):
        power = Power()
        actual = power.getBattery()
        expected = psutil.sensors_battery()
        self.assertEqual(expected,actual)

    def test_isPluggedReturnsBoolean(self):
        power = Power()
        battery = power.getBattery()
        actual = power.isPlugged(battery)
        expected = psutil.sensors_battery()[2]
        self.assertEqual(expected,actual)


    def test_getPercentOfBatteryReturnsFloat(self):
        power = Power()
        battery = power.getBattery()
        actual = power.getPercentOfBattery(battery)
        expected = psutil.sensors_battery()[0]
        self.assertEqual(str(expected),str(actual))