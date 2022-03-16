# Test basic elif statement, part 3

x = 10
y = 20

# if statement stays the same
if x > y:
    print('x is greater than y')

# Add elif conditional statement

elif x != y:
    print('x is not equal to y')
    
# else statement stays the same

else:
    print('x is less than or equal to y')
    

# if, elif and else conditional statements allow for different outcomes depending on which condition is matched
# Only one conditional statement evaluating to True (the first match) will execute
# When True, only that indented code executes once and then exits out of the if/elif/else conditional statement block