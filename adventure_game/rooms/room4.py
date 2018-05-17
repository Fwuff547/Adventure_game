import adventure_game.my_utils as utils

# # # # #
# ROOM 4
#
# Serves as a good template for blank rooms
room4_description = '''
    . . .  4th room ... 
    You wander into a cavern lit by a sliver of moonlight by a crack in the ceiling.
    You see two tunnels leading out one goes west and the other goes south. There's also a door heading east'''
room4_inventory = {
    "key" : 1,
    "torch" : 1
}
room4_locked = {
    "east" : False,
    "west" : True,
    "north" : False,
    "south" : False
}
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room4_description)

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
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == "west":
                is_locked = room4_locked["west"]
                if not is_locked:
                    next_room = 6
                    done_with_room = True
                if is_locked:
                    print("door is locked")
            elif go_where == "south":
                next_room = 8
                done_with_room = True
            elif go_where == "east":
                next_room = 2
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room4_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room4_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room4_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room4_inventory, room4_locked, response)
        else:
            print("The command:", the_command, "has not been implemented in room 4")
        if utils.player_health["health"] < 20:
            utils.player_health["health"] = utils.player_health["health"] + 1
            print("you've been healed one hp by the refreshing light of the blessing of mara")
    return next_room
