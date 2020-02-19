#List - List is a collection of items in a particular order
# List intialize by square brackets []

stocks = ["BX","JPM","C","BAC","WFC"]
print(stocks)

# accessing index position
# Index are started at 0
# access bx position
print(stocks[0])

# Negative index are goes from last elements and reversed
# returns last element WFC
print(stocks[-1])
# returns last element BAC
print(stocks[-2])

# Apply functions to access index
print(stocks[0].lower())

# adding elements to end of the list
stocks.append("SG")
print(stocks)

# insert elements into a list
# insert at index 1 for Goldman Sachs
stocks.insert(1,"GS")
print(stocks)

# removing elements using del()
# removing BX stock from position 0
del stocks[0]
print(stocks)

# removing last elements using pop()
# returns SG removed from the list
stocks.pop()
print(stocks)

#removing element using pop() with index
# return pop(0) expected GS missing from list
stocks.pop(0)
print(stocks)

#removing elements using remove() with value
#returns list without Citi stock
stocks.remove("C")
print(stocks)

#sort list
# Organize the list numerically or alphabetical order
stocks.sort()
print(stocks)
# reverse sorting order with parameter
stocks.sort(reverse=True)
print(stocks)

#sorted - temporaily sorting list using sorted() with parameter as list
tempStock = sorted(stocks)
print(tempStock)

#reverse - reverse the order of the list
print(tempStock.reverse())

#Find the lenght of a list  using len() - Taking list as parameter
size = len(stocks)
print(size)

#Loop with for by index
for stock in stocks:
    print(stock)

# range function range(start,end-1,increament)
# end parameter will stop the loop at size - 1 e.g. size 5 ; end at 4
print("--------")
for i in range(0,len(stocks)):
    print(stocks[i])

listNums = list(range(0,3))


