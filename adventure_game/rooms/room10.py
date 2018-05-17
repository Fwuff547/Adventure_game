import adventure_game.my_utils as utils

# # # # #
# ROOM 10
#
# Serves as a good template for blank rooms
room10_description = '''
    . . .  10th room ... 
    You are in a tall cave, the ceiling is shrouded in darkness and the only sound is the flutter of little,
    leathery wings. There are doors leading north and west.'''
room10_inventory = {}
room10_locked = {
    "east" : False,
    "west" : True,
    "north" : False,
    "south" : False
}
bats_alive =True
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room10_description)
    global bats_alive

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock", "attack"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    bats_health = 6
    bats_atk = 5

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
                is_locked = room10_locked["west"]
                if not is_locked:
                    next_room = 12
                    done_with_room = True
                if is_locked:
                    print("door is locked")
            elif go_where == "north":
                next_room = 8
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room10_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room10_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room10_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room10_inventory, room10_locked, response)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "bats", bats_health, bats_alive, response)
            bats_health = x
            if x <= 0:
                print("the bats are dead")
                bats_alive = False
        else:
            print("The command:", the_command, "has not been implemented in room 10")
        x = utils.creature_action(bats_alive, player_inventory, bats_atk, "bats")
        if x:
            next_room = 666
            done_with_room = True
    return next_room
