# If Statement

stocks = ["BX","JPM","C","BAC","SG","GS","WFC","MTTX","AIG","RBS"]
stocks2 = ["MTTX","LHHMQ","AIG","RBS"]
stock3 = []
# if elif else -> chaining
for stock in stocks:
    if(stock == "BAC"):
        print("%s: RESTRICTED TRADE" % stock)
    elif(stock == "JPM" or stock == "WFC" or stock == "C"):
        print("%s: Competitor Stock; COMPLIANCE APPROVAL REQUIRED" % stock)
    else:
        print("%s: APPROVED TRADEABLE" % stock)

# can run an if elif with the else
    if(stock == "BAC" or stock == "JPM" or stock == "WFC" or stock == "C"):
        print("Big Four Banks")
    elif(stock == "GS"):
        print("Investment Bank")
    elif (stock == "BX"):
        print("Private Equity")

#Checking if List1 is in List2

for stock in stocks2:
    if stock in stocks:
        print("%s Survived outcome of 2007",stock)
    else:
        print("%s Bankrupted",stock)

# check if list is empty
if stock3:
    for stock in stocks:
        print(stock)
else:
    print("Empty List")

#Logical Operators
# C stands for condition
# And (C AND C) => both needs to be true to execute
if(stocks[0] == "BX" and stocks[6] == "WFC"):
    print("BUY")

# OR(C OR C) => only 1 condition needs to be true to execute
if(stocks[0] == "BX" or stocks[2] =="GS"):
    print("BUY")

# Equality comparison
# == Equal C == C
print(2==2)
# > Greater than C>C
print(2>1)
# < Less than C<C
print(1<2)
# >= Greater or equal than C>=C
print(2>=2)
# <= Less or equal than C<=C
print(2<=2)
# != not equal C != C
print(1!=2)