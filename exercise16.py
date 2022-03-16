# lets create a tour of the South West English counties and the tasty treats you could encounter there

treats_by_county = {
    'Cornwall' : 'Cornish Pasty',
    'Devon' : 'Cream Tea',
    'Dorset' : 'Dorset Apple Cake',
    'Somerset' : 'Cheddar Cheese'
}
for key in treats_by_county:
    print('In' , key, 'you should try a bit of' ,treats_by_county[key])