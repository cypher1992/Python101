# While loop runs as or while, a certain condition is satisfied

stock = ["BX","JPM","C","BAC","WFC"]
size = len(stock)
counter = 0

while(counter < size):
    print(stock[counter])
    counter+= 1

# using flag to exit condition

boolean = True

while boolean:
    message = input("Enter Message: ")
    if(message == "exit"):
        boolean = False
    else:
        print(message)

#using break to exit condition
while True:
    message = input("Enter Message: ")
    if(message == "exit"):
        break
    else:
        print(message)

#using continue in a while loop
counter = -1
while(counter < size):
    print(counter)
    if(counter%2 ==0 ):
        counter += 1
        continue
    elif(counter == size-1):
        break
    else:
        counter += 1
        print(stock[counter])

#Looping through a List using While Loop
stock2 = []

while stock:
    stockIndex = stock.pop()
    stock2.append(stockIndex)

print(stock2)

while "BX" in stock2:
    stock2.remove('BX')

print(stock2)
