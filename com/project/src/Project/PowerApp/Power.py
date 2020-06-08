import psutil

class Power:

    def __init__(self):
        battery = self.getBattery()
        plugged = self.isPlugged(battery)
        percent = self.getPercentOfBattery(battery)

    def getBattery(self):
        return psutil.sensors_battery()

    def isPlugged(self, battery):
        return battery[2]

    def getPercentOfBattery(self,battery):
        return str(battery[0])

