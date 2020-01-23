# First Comment
"""
MultiLine Comment
"""

# Variable
value  = 2+2
value2 = (2+1)/2
value3 = (7/3)
value4 = value5 = 5
value6, value7 = 4, -10
pi = 3.1415
radius = 12
area = 0
area = (radius**2)*pi

print(2+2)
print(value)
print(value2)
print(value3)
print(value4 + value5) # 5+5
print(value6)
print(value7)
print(area)


# -------------------

"""Floating Points"""

x = 0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1
y = (x ==1.0)
z = (round(x) == 1)

print(repr(0.5))
print(repr(0.1))
print(x)
print(y)
print(z)

# -------------------

""" String """

str = 'Spam Eggs'
str2 = 'doesn\'t'
str3 = "doesn't"
str4 = '"Yes," he said.'
str5 = "\"Yes,\" he said\""
str6 = "Word" + " Word2 "
str7 = "<" + str6 *5 +  ">"

print(str)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)


nbk = "5123dsa"
hello = "Hello " + nbk
hello2 = "Hello %s" % nbk
print(hello)
print(hello2)

# -------------------

""" SubString String """

word = "String" + 'A'
word1 = "String"[3] #returns i
word2 = "String"[3:5] #returns in
word3 = "String"[3:] #returns ing
word4 = "String"[:3] #returns str
word = word5 = "String2"
wordI = word[:3] + "I" + word[4:] # challenge change i to I

print(word)
print(word1)
print(word2)
print(word3)
print(word4)
print(wordI)




