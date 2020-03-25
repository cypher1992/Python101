"""
List out of bound error try and catch and deal with it
"""

class ListClass(list):

    def __init__(self,list):
        self.list = list

    def getList(self):
        return self.list

    def setList(self,newList):
        self.list = newList

    def findValue(self,value):
        returnObj = None
        for index in self.getList():
             if(value == index):
                 returnObj = value
                 break;
             else:
                 returnObj = None
        return returnObj

    def findValueTryCatch(self,value):
        returnObj = None
        try:
            length = len(self.getList())
            for num in range(0,length):
                if(value == self.list[num]):
                    returnObj = self.list[num]
                    return returnObj
        except Exception as e :
            returnObj =e
        return returnObj
