
from vehicleclasses.Car import Car
from vehicleclasses.Truck import Truck
from simulation.basicsim import BasicSim

from tkinter import *


class MainWindow(object):
    def __init__(self):
        self.sim_LR = BasicSim()
        self.sim_RL = BasicSim()
        self.prev_LR = []
        self.prev_RL = []
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1200, height=200)
        self.canvas.pack()
        self.y = 100
        self.i = 0
        #this call overrides the previous 'canvas.pack'. Remove first.
        self.canvas.pack(fill=BOTH, expand=1)
        self.root.after(0, self.animation)
        self.root.mainloop()

    def animation(self):

        self.canvas.delete("all")
        vehicles_LR = self.sim_LR.step(self.i)
        vehicles_RL = self.sim_RL.step(self.i)
        for vehicle in vehicles_LR:
            self.canvas.create_rectangle(vehicle.position-vehicle.length, self.y, vehicle.position, self.y+50, fill=vehicle.colour)
        for vehicle in vehicles_RL:
            self.canvas.create_rectangle(1200-(vehicle.position - vehicle.length), self.y+100, 1200-vehicle.position, self.y +50, fill=vehicle.colour)
        self.root.after(50, self.animation)
        self.i = self.i + 1

MainWindow()
