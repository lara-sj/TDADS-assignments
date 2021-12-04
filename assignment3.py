import time

colour = input('Your favourite colour: ')
superlative = input('Superlative (ending in \"est\"): ') 
adjective = input('Adjective: ')
body_part_plural = input('Body part (plural): ')
body_part = input('Body part: ')
object = input('Choose an object: ')
food = input('Your favourite food: ')
adjective1 = input('Choose an Adjective: ')
adjective2 = input('Another adjective: ')
adjective3 = input('And one last adjective: ')

time.sleep(1)

print ('The ' + colour + ' Dragon is the ' + superlative + 
        '. It has ' + adjective + ' ' + body_part_plural + 
        ', and a ' + body_part + ' shaped like a ' + object +
        '. It loves to eat ' + food + 
        ', although it will feast on nearly anything. It is ' +
        adjective1 + ' and ' + adjective2 + '. You must be ' +
        adjective3 + ' around it, or you may end up as its meal!')