# Looping Strats over Collections

# Looping over dictionaries

stocks = {"BAC":"Bank Of America", "WFC":"Wells Fargo Corp", "JPM":"JP Morgan"}

for k,v in stocks.items():
    print(k," : ",v)

# Looping over Sequence
for i,v in enumerate(["Item1","Item2","Item3"]):
     print(i," : ",v)

stocks = ["BX","APPL","JPM"]
corp = ["Blackstone","Apple","JP Morgan"]

for s,c in zip(stocks, corp):
    print("Stock: ", s , "\nCorp: ", c)

# Looping Backward
for n in range(0,100,5):
    print(n, end=' ')

print()
for i in reversed(range(0,100,5)):
    print(i, end =" ")
print()

# Looping over sorted index
for i in sorted(set(stocks)):
    print(i)
