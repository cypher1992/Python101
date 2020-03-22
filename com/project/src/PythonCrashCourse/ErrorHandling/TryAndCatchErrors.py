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

