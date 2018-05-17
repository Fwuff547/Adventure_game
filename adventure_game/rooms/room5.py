import adventure_game.my_utils as utils

# # # # #
# ROOM 5
#
# Serves as a good template for blank rooms
room5_description = '''
    . . .  5th room ... 
    You are in a mossy grotto, glow worms on the ceiling dimly illuminate the place.
    there is a ancient oak door with a wrought iron face leading north and a tunnel leading south.'''
room5_inventory = {
    "axe" : 1
}
room5_locked = {
    "east" : False,
    "west" : False,
    "north" : False,
    "south" : False
}
def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room5_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "examine", "status", "unlock"]
    no_args = ["examine", "status"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    print("the face on the door's eyes glow red as it says, in order to pass ye must answer me.")
    response = input("What is it that when you take away the whole, \nyou still have some left over?")
    while not response.lower() == "wholesome":
        print("WRONG!!!!.")
        response = input("Try again. What is it that when you take away the whole, \nyou still have some left over?")
    utils.player_health["health"] = 20
    print("you pass, I have restored you to your full health")
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        response = utils.scrub_response(response)
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == "north":
                next_room = 7
                done_with_room = True
            elif go_where == "south":
                next_room = 3
                done_with_room = True
            else:
                print("That direction is not an option")
        elif the_command == 'take':
            utils.take(player_inventory, room5_inventory, response)
        elif the_command == 'drop':
            utils.drop(player_inventory, room5_inventory, response)
        elif the_command == "status":
            utils.player_status(player_inventory)
        elif the_command == "examine":
            utils.examine(room5_inventory)
        elif the_command == "unlock":
            utils.unlock(player_inventory, room5_inventory, room5_locked, response)
        else:
            print("The command:", the_command, "has not been implemented in room 5")

    return next_room
