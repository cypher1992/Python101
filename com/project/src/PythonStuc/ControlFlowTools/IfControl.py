# If Statement

stockPick = "Blackstone"

if(stockPick == "JP Morgan"):
    print("JPM")
elif(stockPick == "Blackstone"):
    print("BX")
else:
    print("NA")

#---------------------

id = "NA"
id2 = "131411111114"
isin2 = "NA"
isin = "132131132"
list = [id,id2]

def getIsin():
    return isin
def getIsin2():
    return isin2

listID = []
for i in list:
    if(i != "NA"):
        value = i
        listID.append(value)
    else:
        if(getIsin2() != "NA"):
            value = getIsin()
            listID.append(value)
        else:
            value = None
            listID.append(value)

print(listID)

