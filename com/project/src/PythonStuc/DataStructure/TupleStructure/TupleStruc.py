"""
Tuple are immutable
"""

tuple1 = (1)
tuple2 = ('k','v'),(2,3)

print("Tuple1", tuple1)
print("Tuple2", tuple2)

# tuple with and without parentheses

tupleWith = (1,)
tupleWithout = 1,

print("Have the same length ",len(tupleWith), len(tupleWithout))

# Unpacking Tuple and packing tuples

tup3 = (1,2,4)
x,y,z = tup3

print("Tup3", tup3)
print("XYZ",x,y,z)
