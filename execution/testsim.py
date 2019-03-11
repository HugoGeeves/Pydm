from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from execution.parampop import generator_form, car_form, truck_form, simulation_form, inhom_form, specific_inhom_form
from execution.statistics import stats_window
from vehicleclasses.Car import Car
from vehicleclasses.Truck import Truck
from simulation.basicsim import BasicSim

from tkinter import *

LARGE_FONT= ("Verdana", 12)


class MainWindow(object):
    def __init__(self):
        self.sim = BasicSim()
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1200, height=200)
        self.canvas.pack()
        self.animation_state = "STOPPED"

        self.stop = Button(self.root, text="Reset", command=self.stop)
        self.play = Button(self.root, text="Play", command=self.play)
        self.pause = Button(self.root, text="Pause", command=self.pause)
        self.stop.pack()
        self.play.pack()
        self.pause.pack()

        self.graphical = BooleanVar()

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        self.fileMenu = Menu(menubar)
        self.fileMenu.add_checkbutton(label="Graphical", onvalue=True, offvalue=False, variable=self.graphical)
        self.fileMenu.add_command(label="Generator", command=self.generator_parameters)
        self.fileMenu.add_command(label="Car", command=self.car_parameters)
        self.fileMenu.add_command(label="Truck", command=self.truck_parameters)
        self.fileMenu.add_command(label="Simulator", command=self.simulator_parameters)
        menubar.add_cascade(label="Parameters", menu=self.fileMenu)

        self.inhomMenu = Menu(menubar)
        self.inhomMenu.add_command(label="Add Inhomogenous Zone", command=self.inhom_parameters)
        menubar.add_cascade(label="Zones", menu=self.inhomMenu)

        self.y = 100
        self.i = 0
        self.canvas.pack(fill=BOTH, expand=1)
        self.root.after(0, self.animation)
        self.root.mainloop()

    def animation(self):
        if self.animation_state == "PLAY" and self.graphical.get():
            self.canvas.delete("all")
            vehicles = self.sim.step(self.i)
            for vehicle in vehicles:
                self.canvas.create_rectangle(
                    vehicle.position-vehicle.length,
                    self.y,
                    vehicle.position,
                    self.y+50,
                    fill=vehicle.colour
                )

            self.i = self.i + 1

        self.root.after(50, self.animation)

    def stop(self):
        self.animation_state = "STOP"
        self.sim = BasicSim()

        self.canvas.delete("all")

    def pause(self):
        self.animation_state = "PAUSE"

    def play(self):
        self.animation_state = "PLAY"
        if not self.graphical.get():
            for i in range(0, round(self.sim.simulation_length/self.sim.step_size)):
                self.sim.step(i)

        self.sim_end()

    def exit(self):

        self.root.quit()

    def generator_parameters(self):

        win = Toplevel()
        generator_form(self.sim, win)

    def car_parameters(self):

        win = Toplevel()
        car_form(self.sim, win)

    def truck_parameters(self):

        win = Toplevel()
        truck_form(self.sim, win)

    def simulator_parameters(self):

        win = Toplevel()
        simulation_form(self.sim, win)

    def inhom_parameters(self):

        win = Toplevel()
        inhom_form(self, win)

    def specific_inhom(self, zone):

        win = Toplevel()
        specific_inhom_form(self, win, zone)

    def sim_end(self):
        win = Toplevel()
        stats_window(self.sim, win)

    def update_zones(self):
        self.inhomMenu.delete(0, 'end')
        self.inhomMenu.add_command(label="Add Inhomogenous Zone", command=self.inhom_parameters)
        i = 0
        for zone in self.sim.inhom_zones:
            i = i+1
            self.inhomMenu.add_command(label="Inhomogenous Zone"+str(i), command=lambda e=zone: self.specific_inhom(e))






MainWindow()
