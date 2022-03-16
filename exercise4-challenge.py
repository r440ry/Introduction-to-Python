#Do this after demonstrating exercise4.py
#This exercise is for the students to combine what we learned on day one wit input() and if/elif/else statements

x = float(input('Please enter your first number: '))
y = float(input('Please enter your second number: '))

if x > y:
    print('Your first number is greater than your second number.')
    
elif x < y:
    print('Your second number is greater than your first number.')
    
else:
    print('Your numbers are the same.')