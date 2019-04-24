from vehicleclasses.Truck import Truck


class Platoon(Truck):

    size = 5
    follower_gap = 6
    colour = "yellow"

    def __init__(self):
        self.indiv_length = super().length
        self.length = self.indiv_length*self.size
        self.new_velocity = 10
        self.new_position = 0
