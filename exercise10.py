# while loop to create a password checker using break and continue
# You are allowed 3 attempts to guess your password

#password is our stored reference password
password = 'MySecurePassword'
attempt = 0

while attempt < 3:
#    print('What is your password? ')
    password_guess = input('What is your password? ')
    
    if password_guess != password:
        attempt = attempt + 1
        print('\n!!! INCORRECT !!! That was attempt ' + str(attempt) + ' out of 3\n')
        continue
    
    elif password_guess == password:
        print('\nPassword Correct - Access Granted')
        break
    
else:
    print('\nYour password is incorrect and your account has been locked out for 5 minutes')
    
# We use the continue statement to immediately restart the while loop for a wrong password_guess (if statement).
# For a correct password_guess, the else code block runs and then breaks out of the while loop.
# Three wrong guesses causes the 4th conditional while loop statement (3 < 3) to become False and the while loop exits.