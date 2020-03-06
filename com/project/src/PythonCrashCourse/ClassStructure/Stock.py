#Stock Class
#Class has both attributes and methods

class Stock():
    """Model Stock Class"""

    def __init__(self,company,ticker,price,date):
        """Intialize Stock with:
            company
            ticker
            price
            date
        """
        self.company = company
        self.ticker = ticker
        self.price = price
        self.date = date

    #behavior of a stock
    def setCompany(self,newCompany):
        self.company = newCompany

    def setTicker(self,newTicker):
        self.ticker = newTicker

    def setPrice(self,newPrice):
        self.price = newPrice

    def setDate(self,newDate):
        self.date = newDate

    def getCompany(self):
        return self.company

    def getTicker(self):
        return self.ticker

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date


    def updatePriceWithDate(self, newPrice,newDate):
        self.price = newPrice
        self.date  = newDate

        return self

    def toString(self):

        return "Stock Class: {0}, {1}, {2}, {3}".format(self.company,self.ticker,self.price,self.date)

