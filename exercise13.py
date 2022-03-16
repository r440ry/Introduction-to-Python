# Let's create a guess the number game
# We have to guess a random number between 1 and 30 in 5 goes or less
# We need to use the random module so that we can geneate a number using the random.randint() function
import random

#generate a random number between 1 and 30 and assigns it to a variable called random_number
random_number = random.randint(1, 30)

#create the condition for the number of attempts allowed, viz. range(5) = loops of 0,1,2,3,4

for attempts in range(5):
    
    guess = int(input('I am thinking of a number between 1 and 30. Can you guess my number in 5 tries or less? '))
    
    if guess < random_number:
        print('\nyour guess of ' + str(guess) + ' is too low\n')
        continue
        
    elif guess > random_number:
        print('\nyour guess of ' + str(guess) + ' is too high\n')
        continue
        
    elif guess == random_number:
        print('\nWell done, you guessed ' + str(random_number) + ' correctly !!!')
        break
    
else:    
    print('\nUnfortunately, you did not guess my number of ' + str(random_number) + '. Better luck next time!')
    
# per loop we compare if our guess is:
# less than our random_number in the if statement
# greater than our random_number in the first elif statement
# equal to our random_number in the second elif statement
# When we use up all our tries without success the else statement executes once

