
from page_def import Page

from config import *
from style import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import matplotlib as mpl
mpl.use("TkAgg")


class Idle(Page):
    label = None
    data = []
    canvas = None
    p = None

    def change_label(self, text):
        self.label.config(text=text)

    def build_histogram(self):
        self.p.hist(x=self.data, bins=BIN_COUNT, color=chart_color)
        self.p.axes.set_facecolor(background_color)
        self.p.set_title("Heights of Guests in cm", color=text_color)
        self.p.set_ylabel("Frequency", fontsize=24, color=text_color)
        self.p.set_xlabel("Height in cm", fontsize=24, color=text_color)
        self.p.tick_params(colors=text_color)
        self.p.spines['left'].set_color(text_color)
        self.p.spines['bottom'].set_color(text_color)
        self.p.spines['right'].set_color(text_color)
        self.p.spines['top'].set_color(text_color)

    def add_data(self, value):
        self.p.clear()
        self.data.append(value)
        self.build_histogram()
        self.canvas.draw()
        # self.canvas.flush_events()

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        f = Figure(figsize=(5, 5), dpi=100, facecolor=background_color)
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Read in the data during initialization
        try:
            with open("../data/guest_heights.txt", "r") as data_file:
                for line in data_file:
                    self.data.append(float(line.split(",")[1]))
        except:
            print("Could not read data file")

        self.p = f.gca()
        self.build_histogram()
        #self.label = tk.Label(
        #    self, text="Please stand on the spot!", font=("Arial", 60))
        #self.label.pack(side="bottom", fill="x", expand=True)

        self.canvas.draw()
