import generation.basicgen
from simulation.bridgedetector import BridgeDetector
from simulation.compute import acceleration
from simulation.inhomzone import InhomZone
from simulation.pointdetector import PointDetector
from simulation.spacedetector import SpaceDetector


class BasicSim:

    simulation_length = 30
    bridge_length = 1200
    step_size = 0.3

    def __init__(self):
        self.vehicles = []
        self.inhom_zones = []
        self.point_detectors = [PointDetector(150, "flow", 30, False)]
        self.space_detectors = [SpaceDetector(300, 500, "flow", 30, False)]
        self.bridge_detector = [BridgeDetector()]
        self.next_gen_times = 0
        self.t_start = 0
        self.x_start = 0
        self.generator = generation.basicgen.BasicTrafficGen()

    def step(self, i):
        x_end = self.bridge_length
        x_start = self.x_start
        vehicles = self.vehicles
        h = self.step_size
        time = self.t_start + i * h

        try:
            obstruction = vehicles[0].position - vehicles[0].length
        except IndexError:
            obstruction = 200

        if time >= self.next_gen_times and (obstruction > 40):
            vehicles.insert(0, self.generator.next_vehicle())
            self.next_gen_times = time + self.generator.next_headway_interval()

        vehicles.sort(key=lambda obj: obj.position)

        for detector in self.point_detectors:
            detector.record(vehicles, time)
        for detector_space in self.space_detectors:
            detector_space.record(vehicles, time)
        if self.bridge_detector:
            self.bridge_detector[0].record(vehicles, time)

        for index in range(0, len(vehicles)):

            vehicles[index].zone_update(self.inhom_zones)

            if vehicles[index] != vehicles[-1]:
                acc = acceleration(vehicle_a=vehicles[index], vehicle_b=vehicles[index+1])
            else:
                acc = acceleration(vehicle_a=vehicles[index])

            vehicles[index].new_position += h*vehicles[index].velocity
            vehicles[index].new_velocity += h*acc

            if vehicles[index].position > x_end or vehicles[index].position < x_start:
                vehicles.remove(vehicles[index])

        for vehicle in vehicles:
            vehicle.position = vehicle.new_position
            vehicle.velocity = vehicle.new_velocity
        return vehicles

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)
