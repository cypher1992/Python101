class GatherData():

    def getDataSource1(self):
        list = []
        for i in 1000000:
            list.append(i)
        return list

    def getDataSource2(self):
        list = []
        for i in range(100, 1000, 2):
            list.append(i)
        return list

    