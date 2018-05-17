import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms

room3_description = '''
    . . .  3rd room ... 
    You are in a room that feels very familiar. To the NORTH there is a door
    covered in a pale blanket of dust and another door heading west. A snarling kobold stands in front of you. '''
room3_inventory = {
    "spear" : 1
}
kobold_alive =True
room3_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room3_description)
    global kobold_alive

    # valid commands for this room
    commands = ["go", "take", "drop", "examine", "status", "unlock", "attack"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    kobold_health = 12
    kobold_atk_org = 5


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
                next_room = 1
                done_with_room = True
            elif go_where == "north":
                next_room = 5
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room3_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room3_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room3_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room3_inventory, room3_locked, response)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "kobold", kobold_health, kobold_alive, response)
            kobold_health = x
            if x <= 0:
                print("the kobold is dead")
                kobold_alive = False
        else:
            print("The command:", the_command, "has not been implemented in room 3")
        x = utils.creature_action(kobold_alive, player_inventory, kobold_atk_org, "kobold")
        if x:
            next_room = 666
            done_with_room = True
    return next_room

            # END of WHILE LOOP

