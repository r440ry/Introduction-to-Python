# Loop a tuple using the length function

my_tuple = ('tank', 'helicopter', 'hercules')

# We use the len() function to get the number of values in our tuple so that it can be passed to the range function as the number of loops to iterate
for transport in range(len(my_tuple)):
    print('I commute to work by ' + my_tuple[transport])