from vehicleclasses.Truck import Truck


class Platoon(Truck):

    platoon_size = 5
    follower_gap = 6
    colour = "yellow"

    def __init__(self):
        self.indiv_length = super().length
        self.length = self.indiv_length*self.platoon_size
        self.new_velocity = 10
        self.new_position = 0
        self.weight = self.weight*self.platoon_size
