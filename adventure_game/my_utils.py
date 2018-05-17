# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#   valid_options : A list of string values you expect your user to respond with.
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()
def has_a(player_inventory, item):
    if item in player_inventory.keys() and player_inventory[item] >= 1:
        return True
    else:
        return False
weapon_dmg = {
    "knife" : 2,
    "torch" : 2,
    "sword" : 4,
    "spear" : 3,
    "axe" : 4,
}



player_inventory = {

}



def scrub_response(not_array):
    result = []
    result.append(not_array[0])
    if len(not_array) > 1:
        argument = not_array[1]
        if argument == "leather":
            if not_array[2] == "armor":
                result.append("leather armor")
            else:
                prompt_question("that wasn't the right second part, please write armor", ["armor"])
                result.append("leather armor")
        elif argument == "chain":
            if not_array[2] == "armor":
                result.append("chain armor")
            else:
                prompt_question("that wasn't the right second part, please write armor", ["armor"])
                result.append("chain armor")
        elif argument == "plate":
            if not_array[2] == "armor":
                result.append("plate armor")
            else:
                prompt_question("that wasn't the right second part, please write armor", ["armor"])
                result.append("plate armor")
        elif argument == "healing":
            if not_array[2] == "rune":
                result.append("healing rune")
            else:
                prompt_question("that wasn't the right second part, please write rune", ["rune"])
                result.append("healing rune")
        elif argument == "lizard":
            if not_array[2] == "man":
                result.append("lizard man")
            else:
                prompt_question("that wasn't the right second part, please write man", ["man"])
                result.append("lizard man")
        else:
            result.append(argument)
    return result


def armor(player_inventory):
    equipped_armor = 0
    if has_a(player_inventory, "plate armor"):
        equipped_armor = int(equipped_armor + 4)
    elif has_a(player_inventory, "chain mail"):
        equipped_armor = int(equipped_armor + 3)
    elif has_a(player_inventory, "leather armor"):
        equipped_armor = int(equipped_armor + 2)
    if has_a(player_inventory, "helm"):
        equipped_armor = int(equipped_armor + 1)
    return equipped_armor





player_health= {
    "health" : 20
}
defense = armor(player_inventory)

def examine(room_inventory):
    for item in room_inventory.keys():
        print("you see", room_inventory[item], item, "s")


def player_status(player_inventory):
    print("you currently possess: ")
    nothing = True
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            nothing = False
            print("\t\t", key, ":", player_inventory[key])
    if nothing == True:
        print("empty pockets")
    print("you have", player_health["health"], "health")
    print("you have", armor(player_inventory), "defense")




def drop(player_inventory, room_inventory, command):
    drop_what = command[1]
    if has_a(player_inventory, drop_what):
        current_count = player_inventory[drop_what]
        player_inventory[drop_what] = current_count - 1
        if has_a(room_inventory, drop_what):
            room_count = room_inventory[drop_what]
            room_inventory[drop_what] = room_count + 1
        else:
            room_inventory[drop_what] = 1
        print("you dropped the ", drop_what)
    else:
        print("you do no have that item")

def room_status(room_inventory):
    print("\tIn the room you see a ")
    nothing = True
    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            nothing = False
            print("\t\t", key, ",")
    if nothing == True:
        print("lot of air")

def unlock(player_inventory, room_inventory, room_locked, command):
    unlock_what = command[1]
    if has_a(player_inventory, "key"):
        if unlock_what == "east":
            if room_locked["east"]:
                x = prompt_question("do you want to unlock the east door: yes, or no", ["yes", "no"])
                if x == "yes":
                    room_locked["east"] = False
                    print("east room unlocked")
                    player_inventory["key"] = player_inventory["key"] - 1
            else:
                print("that direction is either not locked or not avalible")
        elif unlock_what == "west":
            if room_locked["west"]:
                x = prompt_question("do you want to unlock the west door: yes, or no", ["yes", "no"])
                if x == "yes":
                    room_locked["west"] = False
                    print("west room unlocked")
                    player_inventory["key"] = player_inventory["key"] - 1
            else:
                print("that direction is either not locked or not avalible")
        elif unlock_what == "north":
            if room_locked["north"]:
                x = prompt_question("do you want to unlock the north door: yes, or no", ["yes", "no"])
                if x == "yes":
                    room_locked["north"] = False
                    print("north room unlocked")
                    player_inventory["key"] = player_inventory["key"] - 1
            else:
                print("that direction is either not locked or not avalible")
        elif unlock_what == "south":
            if room_locked["south"]:
                x = prompt_question("do you want to unlock the south door: yes, or no", ["yes", "no"])
                if x == "yes":
                    room_locked["south"] = False
                    print("south room unlocked")
                    player_inventory["key"] = player_inventory["key"] - 1
            else:
                print("that direction is either not locked or not avalible")
        else:
            print("that direction is not registered")
    else:
        print("you don't have any keys")










def take(player_inventory, room_inventory, command):
    take_what = command[1]
    if has_a(room_inventory, take_what):
        room_inventory[take_what] = room_inventory[take_what] - 1
        if has_a(player_inventory, take_what):
            item_count = player_inventory[take_what]
            player_inventory[take_what] = item_count + 1
        else:
            player_inventory[take_what] = 1
        print("you have added a", take_what, "to your inventory")
    else:
        print("you can't take that")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'examine']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        response = response.lower()
        words = response.split()
        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False
                    else:
                        print('\tThe command: "', words[0].lower(), '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.

                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result
#end of ask command
def attack(player_inventory, creature, creature_health, creature_alive, response):
    creature_health_1 = creature_health
    if response[1] == creature:
        if creature_alive:
            weapon = str(input("which weapon do you want to use")).lower()
            if has_a(player_inventory, weapon):
                if creature == "bats":
                    if weapon == "torch":
                        creature_health_1 = int(creature_health_1 - weapon_dmg[weapon])
                        print("you did", weapon_dmg[weapon], "damage to the", creature)
                    else:
                        print("that weapon doesn't hurt the bat swarm")
                else:
                    creature_health_1 = int(creature_health_1 - weapon_dmg[weapon])
                    print("you did", weapon_dmg[weapon], "damage to the", creature)
            else:
                print("you grab for nothing, you don't have that weapon")
                print("you have:")
                for weapon in weapon_dmg.keys():
                    if has_a(player_inventory, weapon):
                        print(weapon)
        else:
            print("congratulations, you just attacked a corpse")
    else:
        print("you attack thin air, that creature is not in the room")
        print("the creature in the room is:", creature)
    return creature_health_1



def creature_action(creature_alive, player_inventory, creature_atk_org, creature):
    death = False
    creature_atk = 0
    defense = armor(player_inventory)
    if creature_alive:
        if defense >= creature_atk_org:
            creature_atk = 0
        elif defense < creature_atk_org:
            creature_atk = int(creature_atk_org - defense)
            player_health["health"] = player_health["health"] - creature_atk
        if player_health["health"] <= 0:
            death = True
        else:
            print("the", creature, "do(es)", creature_atk, "damage to you")
    return death