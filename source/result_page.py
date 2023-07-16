
import tkinter as tk
from page_def import Page


class Result(Page):
    label = None

    def set_height(self, height):
        self.label.config(text="You are " + str(height) + " cm tall!", font=("Arial", 80))

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="both", expand=True)
