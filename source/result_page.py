
import tkinter as tk
from page_def import Page
from config import *
import subprocess

# Unit name : conversion factor to cm
unit_bank = {
    "inches": 2.54,
    "bananas": 17.78,
    "school buses": 1219.2,
    "football fields": 9144,
}
units = list(unit_bank.keys())


class Result(Page):
    label = None
    index = 0

    def set_height(self, height):
        self.index = (self.index + 1) % len(units)
        self.cm_label.config(text="You are " + str(height) +
                             " centimeters tall!", font=("Arial", 80))

        self.alt_label.config(text="That's about " + str(
            round(height / unit_bank[units[self.index]], 2)) + " " + units[self.index] + " tall!", font=("Arial", 60))

    def read_height(self, height):
        msg = "You are " + str(
            round(height / unit_bank[units[self.index]], 2)) + " " + units[self.index] + " tall!"
        cmd = ""
        if OS == "Windows":
            cmd = f'espeak-ng.exe "{msg}"'
        else:
            cmd = "echo \"" + msg + "\" | festival --tts"
        subprocess.Popen(cmd, shell=True)
        

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.cm_label = tk.Label(self, text="")
        self.cm_label.pack(side="top", fill="both", expand=True)
        self.alt_label = tk.Label(self, text="")
        self.alt_label.pack(side="top", fill="both", expand=True)
