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
    
