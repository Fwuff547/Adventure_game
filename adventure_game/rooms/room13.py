import adventure_game.my_utils as utils

# # # # #
# ROOM 13
#
# Serves as a good template for blank rooms
room13_description = '''
    . . .  13th room ... 
    You are in a lit dining hall with a large throne at the end on which sits a massive kobold.
    There is a door leading south and a tunnel with sunlight at the end heading north'''

room13_inventory = {
    "chain armor": 1,
    "sword" : 1,
    "jewel" : 3,
    "spear" : 1
}
room13_locked = {
    "east" : False,
    "west" : False,
    "north" : True,
    "south" : False
}
lizard_man_alive = True
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room13_description)
    global lizard_man_alive

    # valid commands for this room
    commands = ["go", "take", "drop", "examine", "status", "unlock", "attack"]
    no_args = ["examine", "status", ]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    kobold_king_atk = 7
    kobold_king_health = 20

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == "north":
                is_locked = room13_locked["north"]
                if not is_locked:
                    next_room = 547
                    done_with_room = True
                if is_locked:
                    print("door is sealed with special glowing symbols")
            elif go_where == "south":
                next_room = 11
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room13_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room13_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room13_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room13_inventory, room13_locked, response)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "lizard man", kobold_king_health, lizard_man_alive, response)
            kobold_king_health = x + 1.5
            if x <= 0:
                lizard_man_alive = False
                print('''The lizard man falls to the ground with a satisfying thud. His face is locked in a final expression of
                pain and rage before going limp. Victory is yours. The door at the end of the hall's sealing runes fade away.
                ''')
                room13_locked["north"] = False
        else:
            print("The command:", the_command, "has not been implemented in room 13")
        x = utils.creature_action(lizard_man_alive, player_inventory, kobold_king_atk, "lizard man")
        if x:
            next_room = 666
            done_with_room = True
    return next_room
