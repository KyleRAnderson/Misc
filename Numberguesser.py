# Goal: Make a program that generates a number and then has user guess it, with only three attempts.
from random import randint
rndm= randint(0,100)
gNum = 4
while gNum > 0:
    guess= (input('Insert your guess number here:')) #User puts in their number
    if str.isnumeric(guess) == True:
        int(guess)
    else:
        gNum -= 1
        print('I\'m sorry, that\' not a valid number... Try again. You have', (gNum), 'attempt(s) left.')
        continue
    if guess == rndm:
        print('Success! You have guessed the number', rndm)
        break
    else:
        gNum -= 1 #If they're incorrect, we add to the gNum
        print('Sorry. The number', guess, 'is incorrect. You have', (gNum), 'attempt(s) left.')
        continue
if gNum == 0:
     print('Sorry, you have no more attmempts left...')