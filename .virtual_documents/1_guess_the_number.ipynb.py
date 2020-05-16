## 1_ Guess the number project


# Guess the number project
# The user will guess a randomly generated number between 1-20
# Practice: if-else statement
# Library: random

import random
print('Hello. What is your name?')
name = input()
print('Well '+ name + '! I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

# Debug: print('secret number is '+ secretNumber)


# for loop to allow 7 guesses, with hints
for guessesTaken in range(1,7):
    
    print('Take a guess:')
    guess = int(input())
    
    if guess < secretNumber:
        print('your guess is too low.')
    
    elif guess > secretNumber:
        print('your guess is too high')
    
    else: 
        break # this condition is for the correct guess!
    
# print out the guesses and result
if guess == secretNumber:
    print( 'good job ' + name + '! you took '+ str(guessesTaken) + ' guesses.')
    
else:
    print ('Nope. The number i was thining of was ' + str(secretNumber))
    
    



