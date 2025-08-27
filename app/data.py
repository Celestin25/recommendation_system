class house:
    def __init__(self, room, color):
        self.room = room
        self.color = color

    def number_room(self, number):
        print(f"my house has {number} rooms")

    def number_bath_rooms(self, integer):
        print(f"my house has{integer} bathrooms")


flat = house(6, 'green')
store_building = house(8, "blue")
print(store_building.color)
store_building.number_room(6)

