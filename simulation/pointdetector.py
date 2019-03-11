class PointDetector:

    def __init__(self, position, data_type, agg_time_period, microscopic):
        self.position = position
        self.data_type = data_type
        self.aggregation_period = agg_time_period
        self.recorded = []
        self.microscopic_data = []
        self.agg_flows = []
        self.agg_speeds = []
        self.prev_agg = 0
        self.microscopic = microscopic

    def record(self, vehicles, time):
        if self.prev_agg + self.aggregation_period < time:
            self.aggregate(time)
        for vehicle in vehicles:
            if self.is_inside(vehicle):
                self.recorded.append([time, vehicle.velocity])
                self.microscopic_data.append([time, vehicle.velocity])

    def is_inside(self, vehicle):
        if self.position > (vehicle.position - vehicle.length) and self.position < vehicle.position:
            return True
        else:
            return False

    def aggregate(self, time):
        vehicle_amount = len(self.recorded)
        if self.data_type == "Flow":
            current_flow = vehicle_amount * (3600/self.aggregation_period)
            self.agg_flows.append(current_flow)
        elif self.data_type == "Speed":
            total_velocity = 0
            for record in self.recorded:
                total_velocity = total_velocity + record[1]
            if vehicle_amount != 0:
                average_velocity = total_velocity/vehicle_amount
            else:
                average_velocity = 0
            self.agg_speeds.append(average_velocity)


        self.recorded = []
        self.prev_agg = time

    def get_parameter(self, parameter):
        return getattr(self, parameter)

    def update_parameters(self, updates):
        for key, value in updates.items():
            setattr(self, key, value)

