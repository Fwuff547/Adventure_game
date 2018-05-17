import adventure_game.my_utils as utils

# # # # #
# ROOM 8
#
# Serves as a good template for blank rooms
room8_description = '''
    . . .  8th room ... 
    You are in a what appears to be a sort of alchemy lab. There is a door leading north and dark tunnel heading south'''

room8_inventory = {
    "key" : 1,
    "antidote" : 1
}
room8_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room8_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock"]
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
            if go_where == "north":
                next_room = 4
                done_with_room = True
            elif go_where == "south":
                next_room = 10
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room8_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room8_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room8_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room8_inventory, room8_locked, response)
        else:
            print("The command:", the_command, "has not been implemented in room 8")
        if not utils.has_a(player_inventory, "antidote"):
            utils.player_health["health"] = utils.player_health["health"] - 2
            print("your throat is burning and your eyes water, you lose two hp")
            if utils.player_health["health"] <= 0:
                next_room = 666
                done_with_room = True
    return next_room
