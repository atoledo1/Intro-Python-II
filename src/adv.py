from room import Room

from player import Player

from item import Item

from item import LightSource



# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [LightSource("torch", "An old torch")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("sword", "On a closer look, it's plastic")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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



def start_game():
    player = Player("Waverly", room['outside'])

    playing = True

    def player_action(player_input):

        if len(player_input.split()) == 1:

            
            if player_input == "i":
                player.print_items()

            elif player_input == "h":
                player.print_controls()

           
            elif player_input == "l":
                print_surroundings()

          
            elif player_input == "q":
                print("\nGame has been exited!")
                nonlocal playing
                playing = False

          
            elif player_input in ("n", "s", "e", "w"):
                if player.current_room.get_room(player_input) != None:
                    player.current_room = player.current_room.get_room(player_input)
                else:
                    print("\nYou couldn't find a room that direction!")
                    ask_for_input()

           
            else:
                print("\nPlease enter a valid input!")

        else:
            action, item_name = player_input.split()

          
            if action == "get" or action == "take":
                if check_for_light():
                    item = (
                        next((i for i in player.current_room.items if i.name == item_name), None)
                    )
                    if item:
                        player.take_item(item)
                    else:
                        print("\nThere is no item with that name in the room!")
                else:
                    print("\nGood luck finding that in the dark!")


           
            elif action == "drop":
                item = next((i for i in player.items if i.name == item_name), None)
                if item:
                    player.drop_item(item)
                else:
                    print("\nThere is no item with that name in your inventory!")

            
            else:
                print("\nPlease enter a valid input!")

       
        if player_input not in ("n", "s", "e", "w", "q"):
            ask_for_input()


  
    def ask_for_input():
        player_input = input(("\n------\nWhat would you like to do?  " 
            "  (type h for help)\n------\n"))

        player_action(player_input)


    
    def check_for_light():
        if player.current_room.is_light:
            return True

        for i in player.current_room.items:
            if isinstance(i, LightSource):
                return True

        for i in player.items:
            if isinstance(i, LightSource):
                return True

        return False


  
    def print_surroundings():
        print(f"\nYou are in the {player.current_room.name}\n")
        if check_for_light():
            print(player.current_room.description)
            player.current_room.print_items()
        else:
            print("It's pitch black!")


  
    while playing:
        print_surroundings()
        
        ask_for_input()

        print("\n -------------------------------------- \n")

start_game()