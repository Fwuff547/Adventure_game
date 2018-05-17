import adventure_game.my_utils as utils

room1_inventory = {
    "knife" : 1,
}
room1_locked = {
    "east" : True,
    "west" : False,
    "north" : False,
    "south" : False
}

# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 3 (East)
#  Take: There is nothing to take in this room
#  Use: There is nothing to use in this room
#
def run_room(player_inventory):
    description = '''
    . . . Main Room . . .
    You open your eyes. The room you see is unfamiliar. You see a brightly lit
    doorway to the SOUTH. To the EAST you see a closed door. 

    '''
    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock"]
    no_args = ["examine", "status"]


    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        if the_command == 'go':
            direction = response[1].lower()
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                is_locked = room1_locked["east"]
                if not is_locked:
                    next_room = 3
                    done_with_room = True
                if is_locked:
                    print("door is locked")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            utils.take(player_inventory, room1_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room1_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room1_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room1_inventory, room1_locked, response)
    # end of while loop
    return next_room
