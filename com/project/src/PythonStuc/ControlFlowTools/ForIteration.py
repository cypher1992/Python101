# For Iteration

words = ["Hi", "O Boele", "welcome","To" ,"paradise", "city"]
for w in words:
    print(w)

# generate list with range

list = list(range(0,10,2))
print(list)

# range with step argument
for i in range(0,100, 10):
    print(i)

# iterate over indices use range() or len()

sentence = ["Mary", "Had","a","little", "Lamb"]
for i in range(len(sentence)):
    print(i , sentence[i])