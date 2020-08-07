# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def print_controls(self):
        print(("\nControls: \n"
               "  move [n, s, e, w]\n"
               "  look [l]\n"
               "  action [take item_name, get item_name, drop item_name]\n"
               "  inventory [i]\n"
               "  quit [q]\n"))

    def print_items(self):
        print("\nYour Items")
        for i in self.items:
            print(f"  {i}")

    def take_item(self, item):
        self.items.append(item)
        self.current_room.items.remove(item)
        item.on_take()

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)
        item.on_drop()
        self.current_room.print_items()