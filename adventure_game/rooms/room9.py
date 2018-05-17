import adventure_game.my_utils as utils

# # # # #
# ROOM 9
#
# Serves as a good template for blank rooms
room9_description = '''
    . . .  9th room ... 
    You are in a ancient library, your footsteps pick up clouds of dust from the floor. 
    The old tomes almost seem to whisper in the silence. There are doors at either end leading east and west. a comfy chair sits in a corner'''
room9_inventory = {
}
room9_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
mimic_alive = True
def run_room(player_inventory):
    global mimic_alive
    # Let the user know what the room looks like
    print(room9_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "unlock", "attack"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    mimic_health = 10
    mimic_atk = 5

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
                next_room = 7
                done_with_room = True
            elif go_where == "east":
                next_room = 11
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room9_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room9_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room9_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room9_inventory, room9_locked, response)
        elif the_command == "attack":
            x = utils.attack(player_inventory, "mimic", mimic_health, mimic_alive, response)
            mimic_health = x
            if x <= 0:
                print("the mimic is dead")
                mimic_alive = False
        else:
            print("The command:", the_command, "has not been implemented in room 9")
        x = utils.creature_action(mimic_alive, player_inventory, mimic_atk, "mimic")
        if x:
            next_room = 666
            done_with_room = True
        if not mimic_alive:
            utils.health = utils.player_health["health"] + 2
            print("the relaxed feeling o the library heals you 2 hp as you loosen up and your heart rate slows. \nThe smell of old books comforts you, it is friendly magic that's at work here")
    return next_room
