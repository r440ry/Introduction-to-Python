# while loops using a continue statement to skip iteration 1 and then continue as normal

#set number to start at integer 0
number = 0

# Previously, the while loop iterated 3 x
# However, in this example we want to skip an iteration if a conditional if statement is True

while number < 3:
    number = number + 1
    if number == 1:
        continue
    print('The number is ' + str(number))

# Note how we placed 'number = number + 1' before the if statement causing the first iteration value for number to be 1
# Each while loop iteration should print the 'The number is x' where x is the value of number for that iteration
# As 'if number == 1:' on the first iteration is True, Python ignores the print statement 'The number is 1' and immediately starts the 2nd iteration