# room imports
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/./../")
import adventure_game.rooms.room1 as r1
import adventure_game.rooms.room2 as r2
import adventure_game.rooms.room3 as r3
import adventure_game.rooms.room4 as r4
import adventure_game.rooms.room5 as r5
import adventure_game.rooms.room6 as r6
import adventure_game.rooms.room7 as r7
import adventure_game.rooms.room8 as r8
import adventure_game.rooms.room9 as r9
import adventure_game.rooms.room10 as r10
import adventure_game.rooms.room11 as r11
import adventure_game.rooms.room12 as r12
import adventure_game.rooms.room13 as r13
import adventure_game.my_utils as util

from colorama import init
init()
# Default the player to the first room
room_number = 1

print("Welcome to the cavern of the kobold king...\n")


should_continue = True
while should_continue:
    if room_number == 1:
        room_number = r1.run_room(util.player_inventory)
    elif room_number == 2:
        room_number = r2.run_room(util.player_inventory)
    elif room_number == 3:
        room_number = r3.run_room(util.player_inventory)
    elif room_number == 4:
        room_number = r4.run_room(util.player_inventory)
    elif room_number == 5:
        room_number = r5.run_room(util.player_inventory)
    elif room_number == 6:
        room_number = r6.run_room(util.player_inventory)
    elif room_number == 7:
        room_number = r7.run_room(util.player_inventory)
    elif room_number == 8:
        room_number = r8.run_room(util.player_inventory)
    elif room_number == 9:
        room_number = r9.run_room(util.player_inventory)
    elif room_number == 10:
        room_number = r10.run_room(util.player_inventory)
    elif room_number == 11:
        room_number = r11.run_room(util.player_inventory)
    elif room_number == 12:
        room_number = r12.run_room(util.player_inventory)
    elif room_number == 13:
        room_number = r13.run_room(util.player_inventory)
    elif room_number == 666:
        print('''You find yourself looking down at your own body in its expanding pool of blood.
        a tall, skeletal, figure stands beside you. It holds up a drained hourglass.
        In a rattling whisper death says, better luck next time.''')
        break
    elif room_number == 547:
        print('''you emerge into the light of day. You stand atop a snowy mountaintop overseeing a sunny valley. 
        A dark forest stands in the south and a little village with smoke coming out of chimneys sits in the valley surrounded by a flowery meadow.
        You have freed this town from the fear brought by the recent kobold ambushes. 
        Your job here is done. You wander off to get a drink at the local tavern.
        ''')
        break
    else:
        print("Ack I don't know room number:", room_number)
        break

print("The game has ended...")


