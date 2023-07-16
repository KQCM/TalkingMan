
import tkinter as tk
from page_def import Page


class Prompt(Page):
    label = None

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label = tk.Label(
            self, text="Hey I see you there! Stand still!", font=("Arial", 80))
        self.label.pack(side="top", fill="both", expand=True)
