class InhomZone:

    def __init__(self, start, end, new_safe_time_headway):
        self.start = start
        self.end = end
        self.new_safe_time_headway = new_safe_time_headway#

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)