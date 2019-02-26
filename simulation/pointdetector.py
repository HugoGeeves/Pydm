class PointDetector:

    def __init__(self, position, data_type):
        self.position = position
        self.type = data_type
        self.recorded_speeds = []
        self.recorded_times = []

    def record(self, vehicles, time):
        for vehicle in vehicles:
            if self.is_inside(vehicle):
                if self.type is "flow":
                    self.recorded_times.append(time)
                if self.type is "speed":
                    self.recorded_speeds.append(vehicle.velocity)

    def is_inside(self, vehicle):
        if self.position > (vehicle.position - vehicle.length) and self.position < vehicle.position:
            return True
        else:
            return False



