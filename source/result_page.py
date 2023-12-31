
import tkinter as tk
from page_def import Page
from config import *
from style import *
import time
import subprocess

# Unit name : conversion factor to cm
unit_bank = {
    "ice cream cones": 12,
    "jelly beans": 1.27,
    "M&Ms": 1.04,
    "Reeses Cups": 5.08,
    "Mentos": 2.0,
    "Red Vines": 17.0,
    "candy canes": 15.24,
    "gumballs": 2.5,
    "giant jaw breakers": 5.72,
    "Kit Kat": 9.0,
    "Nerds candy": 0.3,
}
units = list(unit_bank.keys())

class Result(Page):
    label = None
    index = 0

    def set_height(self, height):
        self.index = (self.index + 1) % len(units)
        self.cm_label.config(text="You are " + str(round(height, 2)) +
                             " centimeters tall!", font=(text_font, 70),bg=background_color, fg=text_color, wraplength=text_wraplength, justify=text_justify)

        self.alt_label.config(text="That's about " + str(
            round(height / unit_bank[units[self.index]], 2)) + " " + units[self.index] + " tall!", font=(text_font, 60),bg=background_color, fg=text_color, wraplength=text_wraplength, justify=text_justify)

    def read_height(self, height):
        msg_one = "You are " + str(round(height, 2)) + " centimeters tall"
        msg_two = "You are " + str(round(height / unit_bank[units[self.index]], 2)) + " " + units[self.index] + " tall"
        cmd = ""
        if OS == "Windows":
            cmd = f'espeak-ng.exe "{msg}"'
        else:
            cmd0 = "echo \"" + msg_one + "\" | festival --tts"
            cmd1= "echo \"" + msg_two + "\" | festival --tts"
        subprocess.Popen(cmd0, shell=True)
        time.sleep(4)
        subprocess.Popen(cmd1, shell=True)
        

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.cm_label = tk.Label(self, text="")
        self.cm_label.pack(side="top", fill="both", expand=True)
        self.alt_label = tk.Label(self, text="")
        self.alt_label.pack(side="top", fill="both", expand=True)
