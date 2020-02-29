#Functions - blocks of code specified to do one job!
# Write function
# pass parameters
# return a type
# create module files for functions

# simple function: starts with a def name():
def hw():
    print("Hello you SOB")


# passing parameters to a function
def printAdd(num,num2):
    print(str(num+num2))

# function that returns a value
def add(num,num2):
    return num+num2

#using keyvalues to assign values in a function
def addKey(num,num2):
    return  num2+num

#default values in a function and overloading
def add(num,num2,defaultValue=1):
    return defaultValue+num2+num

#making a argument optional
def add(num,num2,defaultValue=0):
    if(defaultValue != 0):
        return defaultValue+num2+num
    else:
        return num + num2

def stockModel(ticker,dailyPrice,company,outstandingShares):
    stock = {"TICKER":ticker,"DAILY_PRICE":dailyPrice,"COMPANY":company,"OUTSTANDING_SHARES":outstandingShares}
    return stock

def printStockKeys(stock):
        length = len(stock)
        counter = 0
        while(counter < length):
            print(stock[counter])
            counter+=1

def rmKeyFromList(index,list):
    head,*tail = list
    def rmAppend(i=index,lst=list,appendList=[]):
        print(len(lst))
        print(i, lst, appendList)
        if(len(lst) >0):
            h, *t = lst
        if(len(lst) == 0):
            return appendList
        elif(i == h):
            rmAppend(i,t,appendList)
        else:
            appendList = appendList.append(h)
            rmAppend(i,t,)
    return rmAppend()


def main():
    #call a function
    hw()
    printAdd(2,2)
    print(str(add(2+2,2)))
    print(addKey(num=2,num2=2))
    print(add(2,3))
    print(add(2,2,3))
    bxStock = stockModel("BX",26.13,"BLACKSTONE",15241)
    keyList = []
    for k,v in bxStock.items():
        print("%s : %s" % (k,v))
        keyList.append(k)

    printStockKeys(keyList)
    rmKeyFromList("TICKER",keyList)

"""----------------------------------------------"""

main()
