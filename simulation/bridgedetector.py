class BridgeDetector:

    def __init__(self):
        self.recorded_speeds = []
        self.record_time = 0
        self.recorded_loads = []

    def record(self, vehicles, time):
            current_load = 0
            for vehicle in vehicles:
                    current_load = current_load + vehicle.weight
            self.recorded_loads.append((time, current_load))

