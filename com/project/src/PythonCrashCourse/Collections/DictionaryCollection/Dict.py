#Dictionary - using dictionary to represent a model such an object
# instantiated with {} braces

# Defining BlackStone Stock
bxStock = {"COMPANY_NAME":"BlackStone","INDUSTRY":"Finance","SUB-INDUSTRY":"Private Equity","PRICE":22.50}
# Accessing Value in Model
print("SUB-INDUSTRY: %s" % bxStock['SUB-INDUSTRY'])

# Adding Values to dictionary
bxStock["SANCTION"] = "NON-SANCTION"
print(bxStock)

#Emtpy Dictionary
gsStock ={}
print("Goldman Sacs Stocks: %s" % gsStock)

# Modifying the Value
bxStock["SUB-INDUSTRY"] = "FinTec"
print(bxStock)

#Looping through a dictionary:
for key,value in bxStock.items():
    print("Key: %s \nValue: %s" % (key,value))

#Looping through keys in dictionary:
for key in bxStock.keys():
    print("Key: %s" % key)

#Looping through keys in order of dictionary:
for key in sorted(bxStock.keys()):
    print("Key: %s" % key)

#Looping through values in dictionary:
for value in bxStock.values():
    print("Value: %s" % value)

# Nesting Collections
# List nested into dictionary
dailyPrice = [22.14,22.16,25.62,30.47,27.91]

bxStock["DailyPrice"] = dailyPrice
print(bxStock)

# Tuple nested into dictionary
hqAddress = ("345 Park Ave", "NY","NY","10154")
bxStock["Address"] = hqAddress
print(bxStock)

#Dictionary in a Dictionary
businesses = {"Hedgefund":"BAAM","Credit":"GSO","Private_Equity":"PE & Strats","Real_Estate":"Real_Estate"}
bxStock["Business_Units"]=businesses
print(bxStock)

gsStock = {"COMPANY_NAME":"Goldman Sachs","INDUSTRY":"Finance","SUB-INDUSTRY":"Investment Banking","PRICE":120.50}
stocks = [bxStock,gsStock]

for stock in stocks:
    for k,v in stock.items():
        print("Key: %s \nValue: %s" % (k,v))