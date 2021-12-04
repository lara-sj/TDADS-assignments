import random
import time 
answer = 'y'
while answer == 'y':
    print(random.randint(1,6)) # while yes, generate and print random number
    time.sleep(0.5) #delay for 0.5 secs between number and next prompt
    answer = input('Roll the dice again? y / n') #ask if user would like to roll again
    time.sleep(0.5) #delay for 0.5 secs between answer and random number
    while answer not in ['y','n']: #if user types something other than y or n
        answer = input('Please type y or n') # ask user to to type y or n
        time.sleep(0.5)