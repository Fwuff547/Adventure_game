import adventure_game.my_utils as utils

# # # # #
# ROOM 7
#
# Serves as a good template for blank rooms
room7_description = '''
    . . .  7th room ... 
    You are in wide hallway. paintings line the wall and torches in brackets cast flickering shadows.
     There are doors to the east and the south. Two snarling wolves stand by the door tethered by a long leash.'''
room7_inventory = {
    "chain armor" : 1
}
room7_locked = {
    "east" : True,
    "west" : False,
    "north" : False,
    "south" : False
}
wolves_alive = True
def run_room(player_inventory):
    # Let the user know what the room looks like
    global wolves_alive
    print(room7_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock", "attack"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    wolves_health = 15
    wolves_atk = 7

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == "south":
                next_room = 5
                done_with_room = True
            elif go_where == "east":
                is_locked = room7_locked["east"]
                if not is_locked:
                    next_room = 9
                    done_with_room = True
                if is_locked:
                    print("door is locked")
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room7_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room7_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room7_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room7_inventory, room7_locked, response)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "wolves", wolves_health, wolves_alive, response)
            wolves_health = x
            if x <= 0:
                print("the wolves are dead")
                wolves_alive = False
        else:
            print("The command:", the_command, "has not been implemented in room 7")
        x = utils.creature_action(wolves_alive, player_inventory, wolves_atk, "wolves")
        if x:
            next_room = 666
            done_with_room = True
    return next_room
