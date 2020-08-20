class ListTicker:


    def __init__(self,tickersPermitted=None,tickersNotPermitted=None):

        if(tickersPermitted != None and tickersNotPermitted != None):
            self.tickersPermitted = tickersPermitted
            self.tickersNotPermitted = tickersNotPermitted
        elif(tickersPermitted == None and tickersNotPermitted != None):
            self.tickersNotPermitted = tickersNotPermitted
        else:
            self.tickersPermitted = tickersPermitted


    def getTickersPermitted(self):
        return self.tickersPermitted

    def getTickersNotPermitted(self):
        return self.tickersNotPermitted

    def setTickersPermitted(self, newTickersPermitted):
        self.tickersPermitted = newTickersPermitted

    def setTickersNotPermitted(self, newTickersNotPermitted):
        self.tickersNotPermitted = newTickersNotPermitted

    def isNotValidTicker(self,ticker):
        if ticker in self.getTickersNotPermitted():
            return True
        else:
            return False