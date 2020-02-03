"""
List common applictions are to:
    1. Iterate or go through sequence of elements with intention to apply operation
    2. Create sub list with condition and apply operation
"""

# create list
square = []

# for loop

for x in range(1,10):
    square.append(x**2)

print("Square List:", square)

# Alternative option using Lambda and Map operation and method

square = list(map(lambda x: x**2, range(1,10)))

print("Lamda Square:", square)

# Alternative option  using Functional Method

square = [x**2 for x in range(1,10)]
print("Functional Square:", square)



