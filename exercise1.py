# Our first program will calculate when you will be eligible to receive your state pension

retirement = 67 #This is an integer

print('What is your name?')    #This just prints something for the user to read on the screen
print() #This prints a blank line

name = input() #Whatever the user types will be assigned to the variable name. input() values are by default strings so bear this in mind.

nameBackwards = name[::-1] #In this line we are going to reverse -1 the whole of the string assigned to name, from the first character : to the last character :

print() #This prints a blank line
print('Hello, ' + name) #We use the print statement to output data to the monitor (standard output). Hello is a string and so is our variable name so they are concatenated
print() #This prints a blank line
print('A fun fact: Did you know that your name backwards is ' + nameBackwards + '?') #Another print statement with concatenation

print() #This prints a blank line
print('How old are you?')    #Ask the user for their age
print() #This prints a blank line

age = input() #Keyboard stroke (std in) are captured as a string and assigned to variable age

timeToRetirement = retirement - int(age) #We create an arithmetic expression here but first we need to change age which is a string to an integer. We do this with int() function
print() #This prints a blank line
print('+' * 79)
print(name + ', you will be eligible for your state pension in ' + str(timeToRetirement) + ' years time.') #Some more string concatenation
print('+' * 79)
