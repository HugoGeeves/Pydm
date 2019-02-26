class PointDetector:

    def __init__(self, position, data_type):
        self.position = position
        self.type = data_type
        self.recorded = []

    def record(self, vehicles, time):
        for vehicle in vehicles:
            if self.is_inside(vehicle):
                self.recorded.append((time, vehicle.velocity))

    def is_inside(self, vehicle):
        if self.position > (vehicle.position - vehicle.length) and self.position < vehicle.position:
            return True
        else:
            return False



