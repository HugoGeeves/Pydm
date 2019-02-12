from math import sqrt


def acceleration(**kwargs):
    # Vehicle a refers to the vehicle in question, b refers to the vehicle in front of it
    vehicle_a = kwargs['vehicle_a']
    vehicle_b = kwargs.get('vehicle_b')

    try:
        free_road_term = vehicle_a.maximum_acceleration*(
                1-((vehicle_a.velocity/vehicle_a.desired_velocity)**vehicle_a.acceleration_exponent)
        )
    except OverflowError:
        print('OHNO')

    if vehicle_b:
        approaching_rate = vehicle_a.velocity - vehicle_b.velocity
        net_distance = vehicle_b.position - vehicle_a.position - vehicle_b.length
        desired_distance = vehicle_a.minimum_spacing + (
                vehicle_a.velocity * vehicle_a.safe_time_headway
        ) + (
                (
                    vehicle_a.velocity * approaching_rate
                ) / (
                    2 * sqrt(vehicle_a.maximum_acceleration * vehicle_a.comfortable_deceleration)
                )
        )

        interaction_term = -vehicle_a.maximum_acceleration*((desired_distance/net_distance)**2)

    else:
        interaction_term = 0

    acc = free_road_term + interaction_term

    return acc


