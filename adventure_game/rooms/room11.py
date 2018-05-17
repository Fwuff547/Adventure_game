import adventure_game.my_utils as utils

# # # # #
# ROOM 11
#
# Serves as a good template for blank rooms
room11_description = '''
    . . .  11th room ... 
    You are in a grungy sleeping room there is a table with cards scattered over it. A group of kobolds sit around the table.
    There are doors leading west and north. A healing pool lies in the corner'''
room11_inventory = {
    "chain armor" : 3,
    "spear" : 3,
    "healing rune" : 1,
    "key" : 1
}
room11_locked = {
    "east" : False,
    "west" : False,
    "north" : True,
    "south" : False
}
kobolds_alive = True
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room11_description)
    global kobolds_alive

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock", "attack"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    kobolds_health = 15
    kobolds_atk = 6

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == "west":
                next_room = 9
                done_with_room = True
            elif go_where == "north":
                is_locked = room11_locked["north"]
                if not is_locked:
                    next_room = 13
                    done_with_room = True
                if is_locked:
                    print("door is locked")
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room11_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room11_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room11_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room11_inventory, room11_locked, response)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "kobolds", kobolds_health, kobolds_alive, response)
            kobolds_health = x
            if x <= 0:
                print("the kobolds are dead")
                kobolds_alive = False
        else:
            print("The command:", the_command, "has not been implemented in room 11")
        x = utils.creature_action(kobolds_alive, player_inventory, kobolds_atk, "kobolds")
        if x:
            next_room = 666
            done_with_room = True
        if utils.has_a(player_inventory, "healing rune"):
            for i in range(3):
                if utils.player_health["health"] < 20:
                    utils.player_health["health"] = utils.player_health["health"] + 1
                print("you've been healed extra for having the healing rune and by the magical pool")
        else:
            for i in range(2):
                if utils.player_health["health"] < 20:
                    utils.player_health["health"] = utils.player_health["health"] + 1
            print("you've been healed for being by the magical pool")
    return next_room
