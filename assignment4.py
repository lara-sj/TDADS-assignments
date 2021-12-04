import numpy as np
import time,os,sys 

delay = 0.5
long_delay = 1

inventory = {'stake':0, 'hammer':0, 'garlic':0}

answer_is_yes = ['y', 'Y', 'yes', 'Yes']
answer_is_no = ['y', 'Y', 'yes', 'Yes']
contin_msg = '(Press \'enter\' to continue)'

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def setup():
    typingPrint('The people of Draynor Village live in constant terror.')
    time.sleep(delay)
    typingPrint('\nTheir numbers are dwindling and the villagers have lost all hope,')
    time.sleep(delay)
    typingPrint('\nall due to the foul creature lurking in the manor to the north known as a vampire.')
    time.sleep(long_delay)
    print('\nYou head north to Draynor Village on a quest to slay the creature.')
    print('\nYou seek help from a retired vampire hunter, Dr Harlow, who you find at the local inn...')
    input(contin_msg)
    global player_name 
    player_name = input('\n Dr Harlow: What is your name, bold adventurer? > ')
    print(f'{player_name}: They call me {player_name}. I have come to help the people of Draynor. Their village is being terrorised by a vampire, but first I need your help... ')
    print('Tell me how to kill it.')
    input(contin_msg)
    print('Dr Harlow: Yes yes.. vampires.. I was very good at killing them once...')
    print('\nWell, you\'re going to need a stake, otherwise he\'ll just regenerate.')
    print('\nYes, you must have a stake to finish it off...')
    print('\nI just happen to have one with me...')
    input(contin_msg)
    typingPrint('Dr Harlow hands you a stake.')
    time.sleep(delay)
    print('\nDr Harlow: You\'ll need a hammer as well, to drive it in properly.')
    input(contin_msg)
    print('\nOne last thing.. It is wise to carry garlic with you.')
    print('\nVampires are somewhat weakened by the smell of garlic.')
    input(contin_msg)
    print('But remember, a vampire is still a dangerous foe!')
    inventory['stake'] = 1
    print ('You have the following items in your inventory: ')
    print (inventory)

def in_room_2():
    typingPrint('You have entered the mansion\'s kitchen.')
    input(contin_msg)
    print('You search the cupboards for garlic, but they are completely empty except for a toolbox.')
    input(contin_msg)
    print('You open the toolbox and find a hammer!')
    inventory['hammer'] = 1
    print ('You have the following items in your inventory: ') 
    print(inventory)

def in_room_3():
    typingPrint('You have entered the study.')
    input(contin_msg)
    print('You inspect the portraits on the walls of the study. Their eyes follow you as you explore the room.')
    time.sleep(delay)
    print('Searching the bookshelf, you find a steel key.')
    take_key = input('Do you take the key? [y/n]? > ')
    if take_key in answer_is_yes:
        inventory['key'] = 1
        print('You now have the following items in your inventory:')
        print(inventory)
    elif take_key in answer_is_no:
        inventory['key'] = 0
    else:
        print('Sorry, I did not understand that. Please type y or n')

def in_room_4():
    typingPrint('You explore the hallway...')
    input(contin_msg)
    print('\nThere are suits of armour on both sides. The helmets glow red in their visors and look toward you as you wander down...')
    take_spade = input('You notice a spade on the floor. Do you want to take the spade? > ')
    if take_spade in answer_is_yes:
            inventory['spade'] = 1
            print('You have the following items in your inventory: ')
            print(inventory)
    elif take_spade in answer_is_no:
        inventory['spade'] = 0
    else: 
        print('Sorry, I did not understand that. Please type y / n ')

def in_room_6():
    typingPrint('You find yourself outside, but it is completely fenced in.')
    input(contin_msg)
    print('You are surrounded by fungus and dead trees. You see a compost heap and an empty fountain with no water.')
    input(contin_msg)
    option_dig()


def in_room_7():
    if inventory['key'] == 1:
        typingPrint('You unlock the door with the steel key and step into the dungeon.')
        input(contin_msg)
        print('The dungeon is littered with barrels, crates and small spiders. There are candle sconces on the walls')
        print('A switch on the wall opens the secret door allowing you to enter through the northern door which leads you back to the hallway in the manor.')
    else: 
        typingPrint('The door is locked. You cannot open it.')
        current_room = 6

def in_room_8():
    typingPrint('You enter the basement.')
    input(contin_msg)
    print('There are tapestries adorning the walls and small candles on the floor.')
    print('There is a coffin at the end of the room.')
    input(contin_msg)
    fight_vampire = input('Are you ready to face Count Draynor? [y/n\?')
    if fight_vampire in answer_is_yes:
        option_fight()
    elif fight_vampire in answer_is_no:
        print('You\'re not ready to fight the vampire and hurry back up the ladder.')
        current_room = 7
    else: 
        print('Sorry, I did not understand that. Please choose y / n')

def option_fight():
    time.sleep(delay)
    print('You walk towards the end of the basement and open the coffin.')
    print('You stab Count Draynor with the stake, awaking him from his peaceful rest.')
    input(contin_msg)
    if inventory['stake'] == 1 & inventory['garlic'] == 1 & inventory['hammer']==1:
        print('He rises from the coffin and lunges for your neck.')
        print('The garlic weakens him and he struggles to fight back.')
        print('You strike the stake with the hammer to drive it in.')
        input(contin_msg)
        print('The Count falls to his knees and turn sinto a statue before collapsing into ashes.')
        time.sleep(delay)
        typingPrint('You have slain the vampire!')
        time.sleep(delay)
        print('\nYou are rewarded 100 coins by the people of Draynor village.')
        print('\nIts inhabitants forever hail you as their hero.')
        
    elif inventory['hammer'] == 0:
        print('You are unable to push the stake far enough in. You need something to drill the stake in to his heart.')
        time.sleep(delay)
        print('Count Draynor lunges for your neck and you die.')
        play_again=input('Do you want to pay again? >')
        if play_again in answer_is_yes:
            setup()
            main()
        elif play_again in answer_is_no:
            quit
        else:
            'Sorry, I did not understand that. Please type y or n.'
    
    elif inventory['garlic'] == 0:
        print('Count Draynor is too strong for you to deal any damage.')
        time.sleep(delay)
        print('He lunges for your neck and you die.')
        play_again=input('Do you want to pay again? >')
        if play_again in answer_is_yes:
            setup()
            main()
        elif play_again in answer_is_no:
            quit
        else:
            'Sorry, I did not understand that. Please type y or n.'

def option_dig():
    if inventory['spade'] == 1:
        typingPrint('You dig up the compost heap and find garlic!')
        inventory['garlic'] = 1
        input(contin_msg)
        print('You now have the following items in your inventory: ')
        print(inventory)
    else: 
        inventory['spade'] = 0
        
    
# list of rooms
def main():
    room_0 = ['Dr Harlow has already given you all the tips he can give you.\n You move onward with your quest...', None, None, 1, None]
    room_1 = ['You arrive at Draynor Manor. The door slams shut behind you. You see a closed door in the east and an archway leading to a dark hallway in the south.', None, 4, 2, 0]
    room_2 = ['You see another door in the south. The western door leads back to the main entrance.', None, 5, None, 1]
    room_3 = ['You spot a ladder going down at the south end of the room. The eastern door leads back to the hallway.', 0, 6, 4, None]
    room_4 = ['Exploring the hallway takes you to the east and west areas of the manor\'s main floor.', 1, None, 5, 3]
    room_5 = ['At the east end of the room, there is a staircase leading down. The western door leads back to the hallway.', 2, 8, None, 4]
    room_6 = ['You notice a door in the east, but it is locked. The door to the north leads you back to the study.', 3, None, 7, None]
    room_7 = ['The secret door on the north side of the dungeon leads to the hallway in the manor. The western door leads outside.', 4, None, None, 6]
    room_8 = ['You leave the basement.', 5, None, None, 8]

# array of rooms
    room_list = np.array([room_0, room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8])
    

# list of accepted directions

    north = ['n', 'N']
    south = ['s', 'S']
    east = ['e', 'E']
    west = ['w', 'W']

    try_again = ('You cannot go this way. Try another direction.')

    current_room = 0

    while True: 
        print('\n')
        print(room_list[current_room][0]) #print room description
        time.sleep(delay)
        chosen_direction = input('Which direction would you like to go? [n / s / e / w] > ')
        if chosen_direction in north:  
            next_room = room_list[current_room][1] #next room should be number for what room is to the north
            if next_room == None:
                print (try_again)
                next_room = current_room
            current_room = next_room

        elif chosen_direction in south:
            next_room = room_list[current_room][2]
            if next_room == None:
                print (try_again)
                next_room = current_room 
            current_room = next_room  


        elif chosen_direction in east:
            next_room = room_list[current_room][3]
            if next_room == None:
                print (try_again)
                next_room = current_room 
            current_room = next_room
    
        elif chosen_direction in west:
            next_room = room_list[current_room][4] 
            if next_room == None:
                print(try_again)
                next_room = current_room
            current_room = next_room
        else: 
            print('Sorry, I did not understand that.')
        
        if current_room == 2:
            in_room_2()

        if current_room == 3:
            in_room_3()
        
        if current_room == 4:
            in_room_4()

        if current_room == 6:
            in_room_6()
        
        if current_room == 7:
            in_room_7()

        if current_room == 8:
            time.sleep(delay)
            in_room_8() 
            break


setup()
main()








