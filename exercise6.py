# while loops using a break statement
# when number counts up to 1 we will break out of our while loop

#set number to start at integer 0
number = 0

# Previously, the while loop iterated 3 x before the condition became False and it exited out of the while loop
# However, in this example we want to break out the while loop if a conditional if statement is True

while number < 3:
    print('The number is ' + str(number))
    if number == 1:
        break
    number = number + 1

# number += 1 is just a shorter way of writing number = number + 1