class GatherData():

    def getDataSource1(self):
        list = []
        for i in range(1000000):
            list.append(i)
        return list

    def getDataSource2(self):
        list = []
        for i in range(100, 1000, 2):
            list.append(i)
        return list

    def getDataSource3(self):
        list = []
        for i in range(10000000, 20000000, 2500):
            list.append(i)
        return list

    def getDataSource4(self):
        list = []
        for i in range(8):
            if (i % 4 == 0):
                list.append(i)
        return list
