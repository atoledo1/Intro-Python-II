from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def start_game():
    player = Player("Waverly", room['outside'])

    print(f"You're name is {player.name}\n")

    playing = True

    def select_room(room, player_input):

        no_room_message = "\nYou couldn't find a room that direction."

        if player_input == "n":
            if not hasattr(room, "n_to"):
                print(no_room_message)
                return room
            return room.n_to

        elif player_input == "s":
            if not hasattr(room, "s_to"):
                print(no_room_message)
                return room
            return room.s_to

        elif player_input == "e":
            if not hasattr(room, "e_to"):
                print(no_room_message)
                return room
            return room.e_to

        elif player_input == "w":
            if not hasattr(room, "w_to"):
                print(no_room_message)
                return room
            return room.w_to

        elif player_input == "q":
            print("\nGame has been exited")
            nonlocal playing
            playing = False
            return room

        else:
            print("\nPlease enter n, s, e, w\n")
            return room


    while playing:
        print(f"You are in the {player.current_room.name} \n")
        print(player.current_room.description)

        player_input = input(
            "\nWhich direction would you like to go? [n, s, e, w] \n")

        player.current_room = select_room(player.current_room, player_input)

        print("\n -------------------------------------- \n")

start_game()