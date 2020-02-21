# If Statement

stocks = ["BX","JPM","C","BAC","SG","GS","WFC"]

for stock in stocks:
    if(stock == "BAC"):
        print("%s: RESTRICTED TRADE" % stock)
    elif(stock == "JPM" or stock == "WFC" or stock == "C"):
        print("%s: Competitor Stock; COMPLIANCE APPROVAL REQUIRED" % stock)
    else:
        print("%s: APPROVED TRADEABLE" % stock)