# while loops using a else statement to do one last action 

#set number to start at integer 0
number = 0

# Previously, the while loop iterated 3 x
# However, in this example we want to break out the normal while loop if a conditional if statement is True

while number < 3:
    print('The number is ' + str(number))
    number = number + 1
else:
    print('The number is now ' + str(number) + ' and has caused the while loop to exit and the else statement to run just this once as it is not indented')