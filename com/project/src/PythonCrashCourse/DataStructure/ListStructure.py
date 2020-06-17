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

    def containValue(self,value):
        if value in self.List:
            return True
        else:
            return False

    def sliceList(self,startIndex,endIndex):
        if(startIndex > len(self.List) | endIndex > len(self.List)):
            return None
        else:
            return self.List[startIndex:endIndex+1]


