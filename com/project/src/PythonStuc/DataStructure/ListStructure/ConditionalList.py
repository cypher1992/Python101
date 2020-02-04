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
