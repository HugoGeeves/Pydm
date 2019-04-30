from vehicleclasses.Car import Car
from vehicleclasses.Platoon import Platoon
from vehicleclasses.Truck import Truck

import random
import math


class BasicTrafficGen:

    flow = 3000

    def __init__(self, lane=0):

        self.lane = lane
        self.car_model = Car
        self.truck_model = Truck
        self.platoon_model = Platoon
        random.seed()

    def next_headway_interval(self):
        minimum_headway = (1/self.flow)*3600
        x = random.uniform(0., 1.)
        t = -1. / 0.9 * math.log((1. - x) / 5.8) + minimum_headway
        return t

    def next_vehicle(self):
        vehicle = random.choices(population=[self.car_model(), self.truck_model(), self.platoon_model()], weights=[0.7, 0.15, 0.15])[0]
        vehicle.lane = self.lane
        vehicle.desired_velocity = self.distribute(vehicle.desired_velocity, vehicle.speed_distribution)
        vehicle.minimum_spacing = self.distribute(vehicle.minimum_spacing, vehicle.spacing_distribution)
        vehicle.weight = self.distribute(vehicle.weight, vehicle.weight_distribution)
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

    @staticmethod
    def distribute(value, distribution):
        st_dev = value/10
        if distribution == "Normal":
            return random.normalvariate(value, st_dev)
        if distribution == "Uniform":
            return random.uniform(value-st_dev, value+st_dev)
        if distribution == "Bimodal":
            dist_one = random.normalvariate(value+(2*st_dev), st_dev)
            dist_two = random.normalvariate(value-(2*st_dev), st_dev)
            return random.choice((dist_one, dist_two))
