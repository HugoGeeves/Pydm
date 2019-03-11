from simulation.inhomzone import InhomZone
from simulation.pointdetector import PointDetector
from simulation.spacedetector import SpaceDetector


def create_zone(sim, params, window, zone=None):
    new_zone = InhomZone(params["zone_start_position"], params["zone_end_position"], params["new_safe_time_headway"])
    if zone:
        sim.sim.inhom_zones.remove(zone)
    sim.sim.inhom_zones.append(new_zone)
    sim.update_zones()
    window.destroy()


def delete_zone(sim, window, zone):
    sim.sim.inhom_zones.remove(zone)
    sim.update_zones()
    window.destroy()


def create_point_detector(sim, params, window, detector=None):
    new_point_detector = PointDetector(params["position"], params["data_type"], params["aggregation_period"],
                                       params["record_microscopic"])
    if detector:
        sim.sim.point_detectors.remove(detector)
    sim.sim.point_detectors.append(new_point_detector)
    sim.update_point_detectors()
    window.destroy()


def delete_point_detector(sim, window, zone):
    sim.sim.point_detectors.remove(zone)
    sim.update_point_detectors()
    window.destroy()


def create_space_detector(sim, params, window, detector=None):
    new_space_detector = SpaceDetector(params["start"], params["end"], params["data_type"], params["aggregation_period"],
                                       params["record_microscopic"])
    if detector:
        sim.sim.point_detectors.remove(detector)
    sim.sim.space_detectors.append(new_space_detector)
    sim.update_space_detectors()
    window.destroy()


def delete_space_detector(sim, window, zone):
    sim.sim.space_detectors.remove(zone)
    sim.update_space_detectors()
    window.destroy()

