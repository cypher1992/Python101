# Dictionary key and value paired = immutable set like tuples

dic = {'BlackStone':'BX','Citi':'C','JP Morgan':'JPM','Bank of America':'BAC'}

print(dic)
# append Wells Fargo
dic['Wells Fargo'] = 'WFC'
print(dic)

# del Blackstone
del dic['BlackStone']
print(dic)
# keys and values
keys = dic.keys()
values = dic.values()

print(keys,values)

# Creating Dictionary with Dict
dicStock = dict(Blackstone = 'BX',Citi = 'C', JP_Morgan ='JPM', Bank_Of_America = 'BAC')
print(dicStock)

#Convert Tuple to Dict
tup1 = ("BlackStone", "BX")
tup2 = ("Citi", "C")
tup3 = ("JP Morgan", "JPM")
tup4 = ("Bank of America", "BAC")

StockList = [tup1,tup2,tup3,tup4]
dicStockTup = dict(StockList)

print("Dic StockList Conversion: ", dicStockTup)
print(dicStockTup['Bank of America'])