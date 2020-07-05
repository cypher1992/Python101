import re
class Regex():

    def __init__(self,string):
        self.string = string

    def getString(self):
        return self.string

    def setString(self,string):
        self.string = string

    def findDigits(self):
        pattern = "[a-ZA-Z]"
        if(re.search(pattern,self.getString())):
            True
        else:
            False