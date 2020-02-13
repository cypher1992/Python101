# Logic Structure

# in
# check if the instance occur sequence

for i in range(0,15,1):
    print(i)

list = [1,4,5,6]
print("\n")

for i in list:
    print(i)

# Is and Is Not
a = 'B'
b = 'A'
# is => compares two objects and returns true if the same and false if not the same
# false
print(a is b)

# is not => compare two objects and returns false if the not the same and true  if the same
print(a is not b)

# Chaining logic comparison

a,b,c = 1,3,3
print(a>b and b==c)
print(a>b==c)

# and -> true and false => false
print(True and False)
# or -> true or false => true
print(True or False)
# not -> not (true and false) = true
# not -> not(true or false) = false
print(not(True and False))
print(not(True or False))
