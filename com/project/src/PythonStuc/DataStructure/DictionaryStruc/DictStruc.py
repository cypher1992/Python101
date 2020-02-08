# Dictionary key and value paired = immutable set like tuples

dic = {'BlackStone':'BX','Citi':'C','JP Morgan':'JPM','Bank of America':'BAC'}

print(dic)
# append Wells Fargo
dic['Wells Fargo'] = 'WFC'
print(dic)

# del Blackstone
del dic['BlackStone']
print(dic)
# keys and values
keys = dic.keys()
values = dic.values()

print(keys,values)