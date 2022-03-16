# Create a program to find the largest number is a list

# create an empty list. We will populate this empty list using the append method in the for loop
list = []

# ask the user to provide a number. We need this number for our range function in our loop.
num = int(input('How many numbers would you like in your list? '))

# iterate the loop for num amount of times. Each iteration append the value to the empty list[]
for i in range(num):
    list_values = int(input('\n' + str(num) + ': Please enter a number: ' ))
    list.append(list_values)
    num = num -1
    print('\nWe are busy building your new list. We have built the following list so far: ' , list)

# print out the newly created list
print('\nYour completed list is: ' + str(list))

# print the largest integer in this list using the max method. You could also use the sort method and then select the last value.
print('\nThe largest integer in this list is:', max(list))

# print the smallest integer in this list using the min method.
print('\nThe smallest integer in this list is:', min(list))