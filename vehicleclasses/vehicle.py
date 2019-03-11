class Vehicle:
    lane = 0
    position = 0
    velocity = 10
    desired_velocity = 30
    safe_time_headway = 1.5
    previous_safe_time_headway = 1.5
    maximum_acceleration = 0.73
    comfortable_deceleration = 1.67
    acceleration_exponent = 4
    minimum_spacing = 2
    length = 5
    colour = "blue"
    in_zone = False

    def zone_update(self, zones):
        for zone in zones:
                if zone.start <= self.position <= zone.end:
                    if not self.in_zone:
                        self.previous_safe_time_headway = self.safe_time_headway
                        self.safe_time_headway = zone.new_safe_time_headway
                        self.in_zone = True
                    return
        self.in_zone = False
        self.safe_time_headway = self.previous_safe_time_headway

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)
