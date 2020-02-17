# String Type
# Strings are wrapped around either double quotation("") or single quotation mark ('')

string = "This is a string"
string2 = 'This is also a string'

# Combining Strings with (+) and New Line Character (\n)
print(string + '\n' + string2)

# Tab Character (\t)
print("\t"+string)

# strObject.title() formats a string to upper case the first letter of every work
name = "robert dI niro"
print(name.title())

# strObject.upper() formats string to change every letter in string to upper case
print(name.upper())

# strObject.lower() formats string to change every letter in string to lower case
print(name.lower())

# strObject.rstrip formats string to remove leading white spaces
stringwithwhitespace = " String "
print("'"+stringwithwhitespace.rstrip()+"'")
# strObject.lstrip formats string to remove prior white spaces
print("'"+stringwithwhitespace.lstrip()+"'")
# strObject.lstrip formats string to remove white spaces
print("'"+stringwithwhitespace.strip()+"'")



