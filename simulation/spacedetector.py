class SpaceDetector:

    def __init__(self, start, end, data_type, time_interval):
        self.start = start
        self.end = end
        self.type = data_type
        self.time_interval = time_interval
        self.recorded_speeds = []
        self.record_time = 0

    def record(self, vehicles, time):
        if time < (self.record_time + self.time_interval):
            return
        current_vehicles = []
        for vehicle in vehicles:
            if self.is_inside(vehicle):
                    current_vehicles.append(vehicle.velocity)
        self.recorded_speeds.append((time, current_vehicles))
        self.record_time = time

    def is_inside(self, vehicle):
        if self.start < vehicle.position < self.end:
            return True
        else:
            return False

