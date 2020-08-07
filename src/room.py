# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, is_light=False):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    def print_items(self):
        if len(self.items) > 0:
            print("\nIn the room you see\n")
            for i in self.items:
                print(f"- {i.name}")

    def get_room(self, direction):
        rooms = { "n": self.n_to, "e": self.e_to, "w": self.w_to, "s": self.s_to }
        return rooms[direction]