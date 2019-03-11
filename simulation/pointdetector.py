class PointDetector:

    def __init__(self, position, data_type, agg_time_period, microscopic):
        self.position = position
        self.type = data_type
        self.agg_time_period = agg_time_period
        self.recorded = []
        self.microscopic_data = []
        self.agg_flows = []
        self.agg_speeds = []
        self.prev_agg = 0
        self.microscopic = microscopic

    def record(self, vehicles, time):
        if self.prev_agg + self.agg_time_period < time:
            self.aggregate(time)
        for vehicle in vehicles:
            if self.is_inside(vehicle):
                self.recorded.append([time, vehicle.velocity])

    def is_inside(self, vehicle):
        if self.position > (vehicle.position - vehicle.length) and self.position < vehicle.position:
            return True
        else:
            return False

    def aggregate(self, time):
        vehicle_amount = len(self.recorded)
        if self.type == "flow":
            current_flow = vehicle_amount * (3600/self.agg_time_period)
            self.agg_flows.append(current_flow)
        elif self.type == "velocity":
            total_velocity = 0
            for record in self.recorded:
                total_velocity = total_velocity + record[1]
            average_velocity = total_velocity/vehicle_amount
            self.agg_speeds(average_velocity)

        if self.microscopic:
            self.microscopic_data.append(self.recorded)
        self.recorded = []
        self.prev_agg = time


