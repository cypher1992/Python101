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

def add(num,num2):
    return num+num2



def main():
    #call a function
    hw()
    printAdd(2,2)
    print(str(add(2+2,2)))

"""----------------------------------------------"""

main()
