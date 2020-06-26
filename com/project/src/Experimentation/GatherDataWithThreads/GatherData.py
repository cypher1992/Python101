import time
class GatherData():

    def getDataSource1(self):
        listNum = []
        for i in range(1000000):
            listNum.append(i)
        time.sleep(1)
        return listNum

    def getDataSource2(self):
        listNum = []
        for i in range(100, 1000, 2):
            listNum.append(i)
        time.sleep(1)
        return listNum

    def getDataSource3(self):
        listNum = []
        for i in range(10000000, 20000000, 2500):
            listNum.append(i)
        time.sleep(1)
        return listNum

    def getDataSource4(self):
        listNum = []
        for i in range(8):
            if (i % 4 == 0):
                listNum.append(i)
        time.sleep(1)
        return listNum
