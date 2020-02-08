# Set - list of objects that are distinct

a = set('abra')
print(a) # only a are distinct along with b r

list = set(['abra','abra','abra','kadabra','alakazam'])
print(list) # removed duplicates of abra

# challenge expected 4 fruits
fruits = ['Apple','Orange','Apple','Orange','Pear','Banana']

count = len(set(fruits))

print(count, set(fruits))