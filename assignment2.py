import random
import time

guesses_taken = 0 #intiate counter for no. of guesses

number = random.randint(1,10) #randomly generate number between 1 and 10

print('I am thinking of a number between 1 and 10')
time.sleep(1) #delay the next line by 1 sec

while guesses_taken<3:
    print('Can you guess the number?') #prompt user to guess number
    guess = input() 
    try:
        guess = float(guess) #check the number is a float
        guesses_taken = guesses_taken + 1
    except ValueError:
        print('Sorry, that\'s not a number between 1 and 10!') #if not a float, print this
        time.sleep(1)
        print('Please give a number between 1 and 10.')
        guess = input()
        guess = float(guess)

    if guess < number: 
        print('That\'s too low.') #if guess is too low, print this
        time.sleep(1)
        if guesses_taken > 0: #if there are any guesses remaining
            print('You have ' + str(3-guesses_taken) + ' guesses remaining.')

    elif guess > number: #if guess is too high, print below
        print ('That\'s too high.')
        time.sleep(1)
        if guesses_taken > 0: #if there are any guesses remaining
            print('You have ' + str(3-guesses_taken) + ' guesses remaining.')

    elif guess == number:
        print ('Correct! You guessed my number.')
        break

if guess != number:
    correct_number = str(number)
    print('Sorry, you have run out of guesses!')
    time.sleep(1)
    print('The number I was thinking of was ' + correct_number)