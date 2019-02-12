class Truck:

    lane = 0
    position = 0
    velocity = 10
    desired_velocity = 30
    safe_time_headway = 2.0
    maximum_acceleration = 0.62
    comfortable_deceleration = 1.67
    acceleration_exponent = 4
    minimum_spacing = 2
    length = 20
    colour = "red"

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)
