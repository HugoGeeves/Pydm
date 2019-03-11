from numpy import mean


class SpaceDetector:

    def __init__(self, start, end, data_type, agg_time_period, microscopic):
        self.start = start
        self.end = end
        self.length = end-start
        self.type = data_type
        self.agg_time_period = agg_time_period
        self.microscopic = False
        self.microscopic_data = []
        self.agg_density = []
        self.agg_speed = []
        self.snapshots = []
        self.prev_agg = 0

    def record(self, vehicles, time):
        if (self.prev_agg + self.agg_time_period) < time:
            self.aggregate(time)

        current_vehicles = []
        for vehicle in vehicles:
            if self.is_inside(vehicle):
                    current_vehicles.append(vehicle.velocity)
        self.snapshots.append((time, current_vehicles))

    def is_inside(self, vehicle):
        if self.start < vehicle.position < self.end:
            return True
        else:
            return False

    def aggregate(self, time):
        snapshot_amount = len(self.snapshots)
        sum_density = 0
        sum_avg_speed = 0

        if self.type == "Flow":
            for snapshot in self.snapshots:
                sum_density = sum_density + (len(snapshot[1])/self.length)
            average_density = sum_density/snapshot_amount
            self.agg_density.append((time, average_density))
        if self.type == "Speed":
            for snapshot in self.snapshots:
                mean_speed = mean(snapshot[1])
                if not mean_speed > 0:
                    mean_speed = 0
                sum_avg_speed = sum_avg_speed + mean_speed
            average_speed = sum_avg_speed/snapshot_amount
            self.agg_speed.append((time, average_speed))

        if self.microscopic:
            self.microscopic_data.append(self.snapshots)
        self.snapshots = []
        self.prev_agg = time

