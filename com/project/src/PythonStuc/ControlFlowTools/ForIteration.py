# For Iteration

words = ["Hi", "O Boele", "welcome","To" ,"paradise", "city"]
for w in words:
    print(w)

# generate list with range

list2 = list(range(0,10,2))
print(list2)

# range with step argument
for i in range(0,100, 10):
    print(i)

# iterate over indices use range() or len()

sentence = ["Mary", "Had","a","little", "Lamb"]
for i in range(len(sentence)):
    print(i , sentence[i])

# Using Enumerate for looping technique
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
list1 = ["Hi","Ho","Hi","Ho","Hi","Ho"]
obj1 = enumerate(list1)
print("Type of obj1", type(obj1))
print(list(obj1))

print(range(0,5))