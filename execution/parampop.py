from tkinter import *
from inflection import underscore

from execution.zone_creator import create_zone, delete_zone, create_point_detector, delete_point_detector, \
    create_space_detector, delete_space_detector
from simulation.inhomzone import InhomZone
from simulation.pointdetector import PointDetector
from simulation.spacedetector import SpaceDetector


def generator_form(sim, window):

    window.title = "Edit Generator Parameters"
    fields = ["Minimum Headway", "Free Vehicle Proportion", "Scale Parameter"]
    variables = make_fields(window, fields, sim.generator)
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         sim.generator.update_parameters(parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def car_form(sim, window):

    window.title = "Edit Car Parameters"
    fields = ["Desired Velocity", "Safe Time Headway", "Maximum Acceleration", "Comfortable Deceleration",
              "Acceleration Exponent", "Minimum Spacing", "Length"]
    variables = make_fields(window, fields, sim.generator.car_model)
    desired_speed_dist = StringVar()
    min_spacing_dist = StringVar()
    weight_dist = StringVar()

    desired_speed_dist.set(sim.generator.car_model.get_parameter(underscore("Speed Distribution").replace(" ", "_")))
    min_spacing_dist.set(sim.generator.car_model.get_parameter(underscore("Spacing Distribution").replace(" ", "_")))
    weight_dist.set(sim.generator.car_model.get_parameter(underscore("Weight Distribution").replace(" ", "_")))

    choices = {'Normal', 'Uniform', 'Bimodal'}

    speed_distribution = OptionMenu(window, desired_speed_dist, *choices)
    spacing_distribution = OptionMenu(window, min_spacing_dist, *choices)
    weight_distribution = OptionMenu(window, weight_dist, *choices, )

    Label(window, text="Speed Distribution").pack(side=TOP, fill=X, padx=5, pady=5)
    speed_distribution.pack(side=TOP, fill=X, padx=5, pady=5)
    Label(window, text="Spacing Distribution").pack(side=TOP, fill=X, padx=5, pady=5)
    spacing_distribution.pack(side=TOP, fill=X, padx=5, pady=5)
    Label(window, text="Weight Distribution").pack(side=TOP, fill=X, padx=5, pady=5)
    weight_distribution.pack(side=TOP, fill=X, padx=5, pady=5)

    variables.append(("Speed Distribution", desired_speed_dist))
    variables.append(("Spacing Distribution", min_spacing_dist))
    variables.append(("Weight Distribution", weight_dist))

    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         sim.generator.car_model.update_parameters(parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def truck_form(sim, window):

    window.title = "Edit Truck Parameters"
    fields = ["Desired Velocity", "Safe Time Headway", "Maximum Acceleration", "Comfortable Deceleration",
              "Acceleration Exponent", "Minimum Spacing", "Length"]
    variables = make_fields(window, fields, sim.generator.truck_model)

    desired_speed_dist = StringVar()
    min_spacing_dist = StringVar()
    weight_dist = StringVar()

    desired_speed_dist.set(sim.generator.truck_model.get_parameter(underscore("Speed Distribution").replace(" ", "_")))
    min_spacing_dist.set(sim.generator.truck_model.get_parameter(underscore("Spacing Distribution").replace(" ", "_")))
    weight_dist.set(sim.generator.truck_model.get_parameter(underscore("Weight Distribution").replace(" ", "_")))

    choices = {'Normal', 'Uniform', 'Bimodal'}

    speed_distribution = OptionMenu(window, desired_speed_dist, *choices)
    spacing_distribution = OptionMenu(window, min_spacing_dist, *choices)
    weight_distribution = OptionMenu(window, weight_dist, *choices, )

    Label(window, text="Speed Distribution").pack(side=TOP, fill=X, padx=5, pady=5)
    speed_distribution.pack(side=TOP, fill=X, padx=5, pady=5)
    Label(window, text="Spacing Distribution").pack(side=TOP, fill=X, padx=5, pady=5)
    spacing_distribution.pack(side=TOP, fill=X, padx=5, pady=5)
    Label(window, text="Weight Distribution").pack(side=TOP, fill=X, padx=5, pady=5)
    weight_distribution.pack(side=TOP, fill=X, padx=5, pady=5)

    variables.append(("Speed Distribution", desired_speed_dist))
    variables.append(("Spacing Distribution", min_spacing_dist))
    variables.append(("Weight Distribution", weight_dist))

    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         sim.generator.truck_model.update_parameters(parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def simulation_form(sim, window):

    window.title = "Edit Simulator Parameters"
    fields = ["Simulation Length", "Bridge Length", "Step Size"]
    variables = make_fields(window, fields, sim)
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         sim.update_parameters(parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def inhom_form(sim, window):

    window.title = "Add inhomogenous zone"
    fields = ["Zone Start position", "Zone End Position", "New Safe Time Headway"]
    variables = make_fields(window, fields, InhomZone, create=True)

    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_zone(sim, parse_entries(e), window)))
    b1.pack(side=LEFT, padx=5, pady=5)


def specific_inhom_form(sim, window, zone):

    window.title = "Edit inhomogenous zone"
    fields = ["Zone Start position", "Zone End Position", "New Safe Time Headway"]
    variables = make_fields(window, fields, zone)
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_zone(sim, parse_entries(e), window, zone=zone)))
    b2 = Button(window, text="Delete",
                command=(lambda z=zone:
                         delete_zone(sim, window, zone)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2.pack(side=LEFT, padx=5, pady=5)


def point_detector_form(sim, window):

    window.title = "Add point detector"
    fields = ["Position", "Aggregation Period"]

    variables = make_fields(window, fields, PointDetector, create=True)
    data_type = StringVar()
    data_type.set("Speed")
    microscopic = BooleanVar()
    rb1 = Radiobutton(window, text="Speed", variable=data_type, value="Speed")
    rb2 = Radiobutton(window, text="Flow", variable=data_type, value="Flow")
    rb3 = Checkbutton(window, text="Record Microscopic", variable=microscopic)
    rb1.pack(side=TOP, fill=X, padx=5, pady=5)
    rb2.pack(side=TOP, fill=X, padx=5, pady=5)
    rb3.pack(side=TOP, fill=X, padx=5, pady=5)
    variables.append(("Data Type", data_type))
    variables.append(("Record Microscopic", microscopic))
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_point_detector(sim, parse_entries(e), window)))

    b1.pack(side=LEFT, padx=5, pady=5)


def specific_point_detector_form(sim, window, detector):
    window.title = "Add point detector"
    fields = ["Position", "Aggregation Period"]

    variables = make_fields(window, fields, detector)
    data_type = StringVar()
    microscopic = BooleanVar()

    data_type.set(detector.get_parameter(underscore("Data Type").replace(" ", "_")))
    microscopic.set(detector.get_parameter(underscore("Microscopic").replace(" ", "_")))

    rb1 = Radiobutton(window, text="Speed", variable=data_type, value="Speed")
    rb2 = Radiobutton(window, text="Flow", variable=data_type, value="Flow")
    rb3 = Checkbutton(window, text="Record Microscopic", variable=microscopic)
    rb1.pack(side=TOP, fill=X, padx=5, pady=5)
    rb2.pack(side=TOP, fill=X, padx=5, pady=5)
    rb3.pack(side=TOP, fill=X, padx=5, pady=5)
    variables.append(("Data Type", data_type))
    variables.append(("Record Microscopic", microscopic))
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_point_detector(sim, parse_entries(e), window, detector=detector)))
    b2 = Button(window, text="Delete",
                command=(lambda d=detector:
                         delete_point_detector(sim, window, detector)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2.pack(side=LEFT, padx=5, pady=5)

def space_detector_form(sim, window):

    window.title = "Add space detector"
    fields = ["Start", "End", "Aggregation Period"]

    variables = make_fields(window, fields, SpaceDetector, create=True)
    data_type = StringVar()
    data_type.set("Speed")
    microscopic = BooleanVar()
    rb1 = Radiobutton(window, text="Speed", variable=data_type, value="Speed")
    rb2 = Radiobutton(window, text="Flow", variable=data_type, value="Flow")
    rb3 = Checkbutton(window, text="Record Microscopic", variable=microscopic)
    rb1.pack(side=TOP, fill=X, padx=5, pady=5)
    rb2.pack(side=TOP, fill=X, padx=5, pady=5)
    rb3.pack(side=TOP, fill=X, padx=5, pady=5)
    variables.append(("Data Type", data_type))
    variables.append(("Record Microscopic", microscopic))
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_space_detector(sim, parse_entries(e), window)))

    b1.pack(side=LEFT, padx=5, pady=5)


def specific_space_detector_form(sim, window, detector):
    window.title = "Add space detector"
    fields = ["Start", "End", "Aggregation Period"]

    variables = make_fields(window, fields, detector)
    data_type = StringVar()
    microscopic = BooleanVar()

    data_type.set(detector.get_parameter(underscore("Data Type").replace(" ", "_")))
    microscopic.set(detector.get_parameter(underscore("Microscopic").replace(" ", "_")))

    rb1 = Radiobutton(window, text="Speed", variable=data_type, value="Speed")
    rb2 = Radiobutton(window, text="Flow", variable=data_type, value="Flow")
    rb3 = Checkbutton(window, text="Record Microscopic", variable=microscopic)
    rb1.pack(side=TOP, fill=X, padx=5, pady=5)
    rb2.pack(side=TOP, fill=X, padx=5, pady=5)
    rb3.pack(side=TOP, fill=X, padx=5, pady=5)
    variables.append(("Data Type", data_type))
    variables.append(("Record Microscopic", microscopic))
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_space_detector(sim, parse_entries(e), window,detector=detector)))
    b2 = Button(window, text="Delete",
                command=(lambda d=detector:
                         delete_space_detector(sim, window, detector)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2.pack(side=LEFT, padx=5, pady=5)


def make_fields(root, fields, object, create=False):
    entries = []
    vcmd = (root.register(validate),
            '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    for field in fields:
        row = Frame(root)
        if not create:
            param = str(object.get_parameter(underscore(field).replace(" ", "_")))
        if isinstance(field, str):
            lab = Label(row, text=field, anchor='w')
            ent = Entry(row, validate='key', validatecommand=vcmd, )
            ent.delete(0, END)
        else:
            if field[0] == "Checkbox":
                lab = Label(row, text=field[1], anchor='w')
                ent = Checkbutton
        if not create:
            ent.insert(0, param)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries



def validate(action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type, widget_name):
    try:
        float(value_if_allowed)
        return True
    except ValueError:
        return False
    else:
        return False


def parse_entries(entries):
    attr_dict = dict()
    for entry in entries:
        attr_name = underscore(entry[0]).replace(" ", "_")
        if attr_name == 'record_microscopic':
            attr_dict[attr_name] = bool(entry[1].get())
        else:
            try:
                attr_dict[attr_name] = float(entry[1].get())
            except ValueError:
                attr_dict[attr_name] = str(entry[1].get())

    return attr_dict
