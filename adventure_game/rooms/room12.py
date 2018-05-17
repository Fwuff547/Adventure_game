import adventure_game.my_utils as utils

# # # # #
# ROOM 12
#
# Serves as a good template for blank rooms
room12_description = '''
    . . .  12th room ... 
    You are in a room with gargantuan roots flowing through it, a key lays trapped in a cage of swirling roots along with a helm.
    There is a door leading east'''

room12_inventory = {

}
room12_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
tree_container = True
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room12_description)
    global tree_container

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock", "attack"]
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
                next_room = 10
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room12_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room12_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room12_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room12_inventory, room12_locked, response)
        elif the_command == "attack":
            if tree_container:
                if response[1] == "tree" or "roots":
                    if utils.has_a(player_inventory, "axe"):
                        print("you chop away the roots revealing the key and helm")
                        room12_inventory["helm"] = 1
                        room12_inventory["key"] = 1
                        tree_container = False
                    else:
                        print("this action requires an axe")
                else:
                    print("your option for attacking is roots")
            else:
                print("you alredy chopped away the roots")
        else:
            print("The command:", the_command, "has not been implemented in room 12")

    return next_room
