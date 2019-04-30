class BridgeDetector:

    def __init__(self):
        self.recorded_speeds = []
        self.record_time = 0
        self.recorded_loads = []
        self.mode = "Microscopic"
        self.highest_load = 0
        self.prev_agg = 0
        self.aggregation_period = 30

    def record(self, vehicles, time):
            current_load = 0
            for vehicle in vehicles:
                    current_load = current_load + vehicle.weight
            if self.mode == "Block Maxima":
                if self.highest_load < current_load:
                    self.highest_load = current_load
                if time >= self.prev_agg+self.aggregation_period:
                    self.recorded_loads.append((time, self.highest_load))
                    self.highest_load = 0
                    self.prev_agg = time
            else:
                self.recorded_loads.append((time, current_load))


    def update_parameters(self, updates):
        for key, value in updates.items():
            setattr(self, key, value)


    def get_parameter(self, parameter):
        return getattr(self, parameter)