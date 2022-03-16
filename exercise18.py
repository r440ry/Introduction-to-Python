# using dictionary keys(), values() and items() methods
house = {
'bedrooms' : 2,
'bathrooms' : 1,
'sq_meters' : 86,
'garden' : True,
'garage' : True,
'price' : 100000,
'rent': 550,
'postcode' : 'PL1 7GT' 
}

# print keys only  
print('Keys only: ')
for k in house.keys():
    print(k)

# separate the output with a blank line
print()

# print values only
print('Values only: ')
for v in house.values():
    print(v)

# separate the output with a blank line
print()

# print keys with values (items)
print('Keys with Values are called Items: ')
for k, v in house.items():
    print('The Key is ' + str(k) + ' and the Value is ' + str(v))