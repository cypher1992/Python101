"""
Using Conditionals for List Composition
"""
# For loop gets x and then get y compare if not equals: return append list
# then increments y and check again after hiting the end of the list
# increments to the next x

list = [(x, y) for x in [1, 2, 3] for y in [3, 4, 1] if x != y]

print(list)

comb = []

for x in [1, 2, 3]:
    for y in [3, 4, 1]:
        if x != y:
            comb.append((x, y))

print(comb)

# Challenge:
vec = [-4, -2, 0, 2, 4]
list = []
# Times 2  the list values
for x in vec:
    list.append(x * 2)
print(list)

newVec = [x * 2 for x in vec]

print(newVec)

# filter list for negatives

filterList = []
for x in vec:
    if (x > -1):
        filterList.append(x)

print(filterList)

filterVec = [x for x in vec if x > -1]
print(filterVec)


# create a function that double an integer
def square(x):
    return x ** 2

applyFunc = []
for x in vec:
    applyFunc.append(square(x))

print(applyFunc)

applyFunc = [square(x) for x in vec]
print(applyFunc)

# call a function that creates a tuples list

tupleList = []
for x in range(1,10):
    tupleList.append((x,x**2))

print("TupleList ", tupleList)

tupleList2 = [(x,x**2) for x in range(1,10)]
print("TupleList 2", tupleList2)

# Nest comprehensize list
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

transcribeRows = [[row[i] for row in matrix] for i in range(4)]

print("Tanscribe",transcribeRows)
matrixList = [tuple(zip(*matrix))]
print("List: ", matrixList)

# Del Statement
# remove an item based on index
# remove items from a list using slice or the entire list

list = [1,2,3,4,5,6,6]
length = len(list) - 1
del list[length]
print("6 removes", list)

del list[:3]
print("List index remove 0 to 2",list)

del list[:]
print("Empty List", list)


