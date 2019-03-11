from vehicleclasses.vehicle import Vehicle


class Car(Vehicle):

    lane = 0
    position = 0
    velocity = 10
    desired_velocity = 30
    safe_time_headway = 1.5
    maximum_acceleration = 0.73
    comfortable_deceleration = 1.67
    acceleration_exponent = 4
    minimum_spacing = 2
    weight = 300
    length = 5
    colour = "blue"

    def __init__(self):
        self.new_velocity = 10
        self.new_position = 0
