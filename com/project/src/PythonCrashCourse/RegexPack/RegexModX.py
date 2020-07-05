import re
class Regex():

    def __init__(self,string):
        self.string = string

    def getString(self):
        return self.string

    def setString(self,string):
        self.string = string

    def findLetters(self):
        pattern = "[a-zA-Z]"
        if(re.search(pattern,self.getString())):
            return True
        else:
            return False