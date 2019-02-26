from vehicleclasses.vehicle import Vehicle


class Truck(Vehicle):

    lane = 0
    position = 0
    velocity = 10

    desired_velocity = 30
    safe_time_headway = 2.0
    maximum_acceleration = 0.62
    comfortable_deceleration = 1.67
    acceleration_exponent = 4
    minimum_spacing = 2
    weight = 1000
    length = 20
    colour = "red"

    def __init__(self):
        self.new_velocity = 10
        self.new_position = 0
