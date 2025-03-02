class Game:
    def __init__(self):
        self.locations = {
            "forest": "You are in a dark forest. There are paths to the north and east.",
            "cave": "You are in a damp cave. There are paths to the west and south.",
            "lake": "You are at the edge of a serene lake. There are paths to the south and west.",
            "mountain": "You are at the base of a towering mountain. There are paths to the north and east."
        }
        self.current_location = "forest"
        self.inventory = []

    def show_location(self):
        print(self.locations[self.current_location])

    def move(self, direction):
        if direction == "north":
            if self.current_location == "forest":
                self.current_location = "mountain"
            elif self.current_location == "cave":
                self.current_location = "forest"
        elif direction == "east":
            if self.current_location == "forest":
                self.current_location = "lake"
            elif self.current_location == "mountain":
                self.current_location = "cave"
        elif direction == "south":
            if self.current_location == "lake":
                self.current_location = "forest"
            elif self.current_location == "cave":
                self.current_location = "mountain"
        elif direction == "west":
            if self.current_location == "cave":
                self.current_location = "forest"
            elif self.current_location == "lake":
                self.current_location = "mountain"
        else:
            print("Invalid direction.")
        self.show_location()

    def take_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"{item} taken.")
        else:
            print(f"You already have {item}.")

    def show_inventory(self):
        print("Inventory:", ", ".join(self.inventory))


def main():
    game = Game()
    game.show_location()

    while True:
        command = input("Enter a command (move, take, inventory, quit): ").strip().lower()
        if command == "move":
            direction = input("Enter a direction (north, south, east, west): ").strip().lower()
            game.move(direction)
        elif command == "take":
            item = input("Enter an item to take: ").strip().lower()
            game.take_item(item)
        elif command == "inventory":
            game.show_inventory()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
