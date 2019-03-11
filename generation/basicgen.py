from vehicleclasses.Car import Car
from vehicleclasses.Platoon import Platoon
from vehicleclasses.Truck import Truck

import random
import math


class BasicTrafficGen:

    minimum_headway = 1.2
    free_vehicle_proportion = 5.8
    scale_parameter = 0.9

    def __init__(self, lane=0):

        self.lane = lane
        self.car_model = Car
        self.truck_model = Truck
        self.platoon_model = Platoon
        random.seed()

    def next_headway_interval(self):
        x = random.uniform(0., 1.)
        t = -1./self.scale_parameter * math.log((1. - x)/self.free_vehicle_proportion) + self.minimum_headway
        return t

    def next_vehicle(self):
        vehicle = random.choices(population=[self.car_model(), self.truck_model(), self.platoon_model()], weights=[0.8, 0.1, 0.1])[0]
        vehicle.lane = self.lane
        vehicle.desired_velocity = random.gauss(vehicle.desired_velocity, 4.)
        vehicle.safe_time_headway = vehicle.safe_time_headway + random.paretovariate(3.)
        vehicle.maximum_acceleration = random.gauss(vehicle.maximum_acceleration, 0.05)
        vehicle.comfortable_deceleration = random.gauss(vehicle.comfortable_deceleration, 0.05)
        return vehicle

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)
