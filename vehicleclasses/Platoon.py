from vehicleclasses.Truck import Truck


class Platoon(Truck):

    weight = 1000
    length = 60
    colour = "yellow"

    def __init__(self):
        self.new_velocity = 10
        self.new_position = 0
