class InhomZone:

    def __init__(self, start, end, new_safe_time_headway):
        self.zone_start_position = start
        self.zone_end_position = end
        self.new_safe_time_headway = new_safe_time_headway#

    def get_parameter(self, parameter):
        return getattr(self, parameter)

    def update_parameters(self, updates):
        for key, value in updates.items():
            setattr(self, key, value)
