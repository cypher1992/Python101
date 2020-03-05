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
    def updatePriceWithDate(newPrice,newDate):
        price = newPrice
        date = newDate

        return price,date
