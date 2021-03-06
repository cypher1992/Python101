# List

# -------------------

""" List """

list = ['A','B','C']

# Slicing
# We use the colon (:) to slice lists.

listAB = list[:2]
list3Times = listAB*2

# removing index
list[0:1] = []
print('list remove ',list)

# insert index into list at position 1 or after b
index = 'D'
list[1:1] = [index]
print('list Insert',list)

#insert at the beginning of the list
cplist = list
cplist[:0] = index
print('Insert D at the being of the list', cplist)

#empty list
list[:] = []
print("Empty List", list)

# List Pop Index 2
list = ['A','B','C','D']
popIndex1 = list.pop(1)
print("Pop Index 1 or Letter B", list)

# List Remove Index 2
list = ['A','B','C','D']
removeIndex = list.remove('D')
print("Remove D", list)


#Nested List
list1 = [1,2,3]
list2 = [100,list1,200,300]

print("Nested List: ",list2)
# Append
list2[1].append(4)
print("Nested List ",list2)

#insert(position,indexItem) | NOTE: returns None Only modify Mutable data strucuture
list = [1,2,4,5]
list.insert(1,200)
print("Insert List Func ",list)

#remove(firstInstanceOfValue)
list = [1,2,3,4,5,6,5]
rm = list.remove(5)
print(rm)

#pop()
# pop list.pop(num) => return list with the position removed
# pop list.pop() => last element is removed and return the previous

list.pop(0)
list.pop()
print("ListPop", list)

#clear() => clears all Elements in the list
clearList = list.clear()
print(clearList)

#index('searchValue',Start,End)
# searchValue -> looking for specified value
# start -> startOfSubList
# end ->  endOfSubList
list = ["Alpha","Beta","Charlie","Delta","Alpha","Echo"]


alphasubSearch = list.index("Alpha",4,5)
print("AlphaSub:", alphasubSearch)
betaSearch = list.index("Beta",)
print("Beta:", betaSearch)

#COUNT => number of time a object appears in the list
alphaCount = list.count("Alpha")
print("Number of instance for Alpha: ",alphaCount)

#sort(key=none,reverse=false) => sort list | NOTE: returns None Only modify Mutable data strucuture
list.sort(key=len)
print("Sort List with Len Key: ", list)

#sorted(list,key=none) => sortlist
alphaBet = ['A','Z','E']
sortedList = sorted(alphaBet)
print("Sorted List: ", sortedList)
sortedWithKey = sorted(list,key=len)
print("Sorted List with Key",sortedWithKey)

#reverse() => reverse a list | NOTE: returns None Only modify Mutable data strucuture
sortedWithKey.reverse()
print("Reverse Sorted List with Key", sortedWithKey)

#copy() => copy a list
listCopy = list.copy()
print("Copy List", listCopy)

#Get index 1 of the nested list
value2 = list2[1][1]
print("Value should equal 2 =",value2)

print("-------------------------------------")

print(list, type(list))
print(listAB)
print(list3Times)


for a in list:
    print(a)


## Assignment
days = ["Fri","Sat","Sun","Mon","Tue","Wed","Thur"]
lengthOfDays = len(days)
# print Mon
mon = days[3:4]
Mon = days[3]

print("DAY: ", mon, Mon)