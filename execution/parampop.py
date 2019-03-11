from tkinter import *
from inflection import underscore

from execution.zone_creator import create_zone, delete_zone
from simulation.inhomzone import InhomZone


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
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         sim.generator.car_model.update_parameters(parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def truck_form(sim, window):

    window.title = "Edit Truck Parameters"
    fields = ["Desired Velocity", "Safe Time Headway", "Maximum Acceleration", "Comfortable Deceleration",
              "Acceleration Exponent", "Minimum Spacing", "Length"]
    variables = make_fields(window, fields, sim.generator.truck_model)
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
                         create_zone(sim, parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def specific_inhom_form(sim, window, zone):

    window.title = "Edit inhomogenous zone"
    fields = ["Zone Start position", "Zone End Position", "New Safe Time Headway"]
    variables = make_fields(window, fields, zone)
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_zone(sim, parse_entries(e))))
    b2 = Button(window, text="Delete",
                command=(lambda z=zone:
                         delete_zone(sim, window, zone)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2.pack(side=LEFT, padx=5, pady=5)


def point_detector_form(sim, window):

    window.title = "Add point detector"
    fields = ["Position", "Aggregation Period"]
    variables = make_fields(window, fields, InhomZone, create=True)
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_zone(sim, parse_entries(e))))
    b1.pack(side=LEFT, padx=5, pady=5)


def specific_point_detector_form(sim, window, zone):

    window.title = "Edit point detector"
    fields = ["Position", "Aggregation Period"]
    variables = make_fields(window, fields, zone)
    b1 = Button(window, text='Save',
                command=(lambda e=variables:
                         create_zone(sim, parse_entries(e))))
    b2 = Button(window, text="Delete",
                command=(lambda z=zone:
                         delete_zone(sim, window, zone)))
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

def make_detector_fields()


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
        attr_dict[attr_name] = float(entry[1].get())

    return attr_dict
