# As a reminder this was our while loop from exercise 5 to loop our indented code 3 times (0,1,2):

# number = 0
# while number < 3:
#    print('The number is ' + str(number))
#    number = number + 1

# For comparison we will loop our indented code 3 times using a for loop with the range command (0,1,2) to create the same result:

for number in range(5):
    print('The number is ' + str(number))

# We use range() command as it provides a simple way to count the number of loops/iterations we want to run.

# The for loop iterates over items. Here we will iterate over letters in a string/word:

# name = 'Rory Grant'
# for letters in name:
#     print(letters)