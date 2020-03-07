# Inheritence

import uuid

class Security():
    def __init__(self,price,date):
        self.date = date
        self.price = price
        self.id = uuid.uuid1().version


    def setPrice(self, newPrice):
        self.price = newPrice

    def setDate(self, newDate):
        self.date = newDate

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date

    def getID(self):
        return self.id