from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from execution.parampop import generator_form, car_form, truck_form, simulation_form
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

        fileMenu = Menu(menubar)
        fileMenu.add_checkbutton(label="Graphical", onvalue=True, offvalue=False, variable=self.graphical)
        fileMenu.add_command(label="Generator", command=self.generator_parameters)
        fileMenu.add_command(label="Car", command=self.car_parameters)
        fileMenu.add_command(label="Truck", command=self.truck_parameters)
        fileMenu.add_command(label="Simulator", command=self.simulator_parameters)
        menubar.add_cascade(label="Parameters", menu=fileMenu)

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
            for i in range(0, 1000):
                self.sim.step(i)
                print(i)




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

        win = Toplevel
        simulation_form(self.sim, win)

    def graph_page(self, data, title):

        t = Toplevel(self.root)
        label = Label(t, text=title, font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot(data)

        canvas = FigureCanvasTkAgg(f, t)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

MainWindow()