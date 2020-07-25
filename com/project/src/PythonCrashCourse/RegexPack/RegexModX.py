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

    def matchPatterns(self,pattern=r'abc'):
            patternX = re.compile(pattern)
            listMatch = []
            for match in patternX.finditer(self.getString()):
                listMatch.append(match.start())
                listMatch.append(match.group())
            return listMatch

    def matchPatternsGroups(self,pattern=r'abc',index = 0):
            patternX = re.compile(pattern)
            listMatch = []
            for match in patternX.finditer(self.getString()):
                try:
                    listMatch.append(match.group(index))
                except IndexError:
                    break
            return listMatch

    def pureMatchPatterns(self,pattern=r'abc'):
            patternX = re.compile(pattern)
            listMatch = []
            for match in patternX.finditer(self.getString()):
                listMatch.append(match.group())
            return listMatch