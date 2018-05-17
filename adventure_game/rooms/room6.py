import adventure_game.my_utils as utils
room6_inventory = {
    "plate armor" : 1,
    "sword" : 1,
    "knife" : 2
}

room6_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
# # # # #
# ROOM 6
#
# Serves as a good template for blank rooms
room6_description = '''
    . . .  6th room ... 
    You are in a room that appears to be an armory. there is a door to the east'''



def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room6_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "examine", "status", "unlock"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == "east":
                next_room = 4
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room6_inventory, response)
            print("debug response", response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room6_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room6_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room6_inventory, room6_locked, response)
        else:
            print("The command:", the_command, "has not been implemented in room 6")
    return next_room
