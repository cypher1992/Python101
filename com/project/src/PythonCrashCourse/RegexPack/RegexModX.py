import re
class Regex():

    def __init__(self,string):
        self.string = string

    def getString(self):
        return self.string

    def setString(self,string):
        self.string = string

    def isAllLetters(self,pattern="^[a-zA-Z]+$"):
        if(re.search(pattern,self.getString())):
            return True
        else:
            return False

    def isPatternOf(self,pattern = "[a-zA-Z]"):
        if (re.search(pattern, self.getString())):
            return True
        else:
            return False

    def setupReCompile(self,pattern=r'abc'):
            patternX = re.compile(pattern)
            matches = patternX.finditer(self.getString())
            return matches