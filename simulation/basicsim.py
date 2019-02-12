import generation.basicgen
from simulation.compute import acceleration


class BasicSim:

    simulation_length = 30
    bridge_length = 1200
    step_size = 0.3

    def __init__(self):
        self.vehicles = []
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

        if time >= self.next_gen_times:
            vehicles.insert(0, self.generator.next_vehicle())
            self.next_gen_times = time + self.generator.next_headway_interval()

        vehicles.sort(key=lambda obj: obj.position)

        for index in range(0, len(vehicles)):
            if vehicles[index] != vehicles[-1]:
                acc = acceleration(vehicle_a=vehicles[index], vehicle_b=vehicles[index+1])
            else:
                acc = acceleration(vehicle_a=vehicles[index])

            vehicles[index].position += h*vehicles[index].velocity
            vehicles[index].velocity += h*acc

            if vehicles[index].position > x_end or vehicles[index].position < x_start:
                vehicles.remove(vehicles[index])

        return vehicles

    @classmethod
    def update_parameters(cls, updates):
        for key, value in updates.items():
            setattr(cls, key, value)

    @classmethod
    def get_parameter(cls, parameter):
        return getattr(cls, parameter)
