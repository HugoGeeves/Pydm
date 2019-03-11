from simulation.inhomzone import InhomZone
from simulation.pointdetector import PointDetector
from simulation.spacedetector import SpaceDetector


def create_zone(sim, params):
    new_zone = InhomZone(params["zone_start_position"], params["zone_end_position"], params["new_safe_time_headway"])
    sim.sim.inhom_zones.append(new_zone)
    sim.update_zones()


def delete_zone(sim, window, zone):
    sim.sim.inhom_zones.remove(zone)
    sim.update_zones()
    window.destroy()

def create_point_detector(sim, params):
    new_point_detector = PointDetector(params[""], params[""], params[""])

def delete_point_detector(sim, window, zone):
    sim.sim.inhom_zones.remove(zone)
    sim.update_zones()
    window.destroy()

def create_space_detector(sim, params):
    new_space_detector = SpaceDetector(params[""], params[""], params[""])

def delete_space_detector(sim, window, zone):
    sim.sim.inhom_zones.remove(zone)
    sim.update_zones()
    window.destroy()

