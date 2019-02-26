from tkinter import *
from inflection import underscore


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

def imhom_form(sim, window):

    window.title = "Add imomogenous zone"
    fields = ["Zone Start position", "Zone End Position", "New Safe Time Headway"]

def make_fields(root, fields, object):
    entries = []
    vcmd = (root.register(validate),
            '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    for field in fields:
        row = Frame(root)
        param = str(object.get_parameter(underscore(field).replace(" ", "_")))
        lab = Label(row, text=field, anchor='w')
        ent = Entry(row, validate='key', validatecommand=vcmd, )
        ent.delete(0, END)
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
        attr_dict[attr_name] = float(entry[1].get())

    return attr_dict
