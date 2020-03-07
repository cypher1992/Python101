#Stock Class
#Class has both attributes and methods

from com.project.src.PythonCrashCourse.ClassStructure.Security import Security

class Stock(Security):
    """Model Stock Class"""

    def __init__(self,company,ticker,price,date):
        """Intialize Stock with:
            company
            ticker
            price
            date
        """
        super().__init__(price,date)
        self.company = company
        self.ticker = ticker

    #behavior of a stock
    def setCompany(self,newCompany):
        self.company = newCompany

    def setTicker(self,newTicker):
        self.ticker = newTicker

    def getCompany(self):
        return self.company

    def getTicker(self):
        return self.ticker

    def updatePriceWithDate(self, newPrice,newDate):
        self.price = newPrice
        self.date  = newDate

        return self

    def toString(self):

        return "Stock Class: {0}, {1}, {2}, {3}".format(self.company,self.ticker,self.price,self.date)

