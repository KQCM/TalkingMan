
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from page import Page
import numpy as np
import matplotlib
matplotlib.use("TkAgg")


class BarChart(Page):

    label = None
    data = np.random.normal(100, 30, 40).tolist()
    canvas = None
    p = None

    def change_label(self, text):
        self.label.config(text=text)
        

    def add_data(self, value):
        self.p.clear()
        self.data.append(value)
        self.p.hist(self.data, 100)
        self.canvas.draw()
        # self.canvas.flush_events()

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        f = Figure(figsize=(5, 10), dpi=100)
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.p = f.gca()
        self.p.hist(self.data, 100)
        self.p.set_title("Heights of Guests in cm")
        self.p.set_ylabel("Frequency", fontsize=24)
        self.p.set_xlabel("Height in cm", fontsize=24)

        self.label = tk.Label(
            self, text="Please stand on the spot!", font=("Arial", 40))
        self.label.pack(side="bottom", fill="x", expand=True)

        self.canvas.draw()
