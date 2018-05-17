import adventure_game.my_utils as utils

room2_inventory = {
    "key" : 1,
    "leather armor" : 1,
}
room2_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
rat_alive = True
# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    global rat_alive
    description = '''
    . . . 
    You are in a brightly lit room. The room appears to be an office. There are doors exiting heading west and north.
    There is a large rat lying on the table.'''

    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "examine", "status", "attack", "unlock"]
    no_args = ["examine", "status"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1
    rat_health = 5
    rat_atk_org = 3

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        if the_command == 'go':
            direction = response[1].lower()
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                done_with_room = True
            elif direction == "west":
                next_room = 4
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go", direction)
        elif the_command == 'take':
            utils.take(player_inventory, room2_inventory, response)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room2_inventory, room2_locked, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room2_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room2_inventory)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "rat", rat_health, rat_alive, response)
            rat_health = x
            if x <= 0:
                print("the rat is dead")
                rat_alive = False
        else:
            print("Command not implemented in ROOM 2,", the_command)
        x = utils.creature_action(rat_alive, player_inventory, rat_atk_org, "rat")
        if x:
            next_room = 666
            done_with_room = True
    # end of main while loop
    return next_room

