import psutil

class Power:

    def getBattery(self):
        return psutil.sensors_battery()

    def isPlugged(self, battery):
        return battery[2]

    def getPercentOfBattery(self, battery):
        return str(battery[0])

