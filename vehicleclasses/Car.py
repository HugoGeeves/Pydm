class Car:

    lane = 0
    position = 0
    velocity = 10
    desired_velocity = 30
    safe_time_headway = 1.5
    maximum_acceleration = 0.73
    comfortable_deceleration = 1.67
    acceleration_exponent = 4
    minimum_spacing = 2
    length = 5
    colour = "blue"

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)
