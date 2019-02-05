from vehicleclasses.Car import Car
from vehicleclasses.Truck import Truck

import random
import math




class BasicTrafficGen:

    def __init__(self, lane=0):
        self.minimum_headway = 1.2
        self.free_vehicle_proportion = 5.8
        self.scale_parameter = 0.9
        self.lane = lane
        random.seed()

    def next_headway_interval(self):
        x = random.uniform(0., 1.)
        t = -1./self.scale_parameter * math.log((1. - x)/self.free_vehicle_proportion) + self.minimum_headway
        return t

    def next_vehicle(self):
        vehicle = random.choices(population=[Car(), Truck()], weights=[0.9, 0.1])[0]
        vehicle.lane = self.lane
        vehicle.desired_velocity = random.gauss(vehicle.desired_velocity, 4.)
        vehicle.safe_time_headway = vehicle.safe_time_headway + random.paretovariate(3.)
        vehicle.maximum_acceleration = random.gauss(vehicle.maximum_acceleration, 0.05)
        vehicle.comfortable_deceleration = random.gauss(vehicle.comfortable_deceleration, 0.05)
        return vehicle
