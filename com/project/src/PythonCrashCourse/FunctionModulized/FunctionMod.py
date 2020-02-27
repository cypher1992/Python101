#Functions - blocks of code specified to do one job!
# Write function
# pass parameters
# return a type
# create module files for functions

# simple function: starts with a def name():
def hw():
    print("Hello you SOB")


# passing parameters to a function
def printAdd(num,num2):
    print(str(num+num2))

# function that returns a value
def add(num,num2):
    return num+num2

#using keyvalues to assign values in a function
def addKey(num,num2):
    return  num2+num



def main():
    #call a function
    hw()
    printAdd(2,2)
    print(str(add(2+2,2)))
    print(addKey(num=2,num2=2))

"""----------------------------------------------"""

main()
