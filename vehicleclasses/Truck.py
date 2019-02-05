class Truck:

    def __init__(self):
        self.lane = 0
        self.position = 0
        self.velocity = 10
        self.desired_velocity = 30
        self.safe_time_headway = 2.0
        self.maximum_acceleration = 0.62
        self.comfortable_deceleration = 1.67
        self.acceleration_exponent = 4
        self.minimum_spacing = 2
        self.length = 20
        self.colour = "red"
