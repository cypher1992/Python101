class List():

    def __init__(self,list):
        self.List = list

    def getList(self):
        return self.List

    def setList(self,newList):
        self.List = newList

    def appendToList(self,value):
        return self.List.append(value)

    def removeValue(self,value):
        return self.List.remove(value)


