
import tkinter as tk
from page import Page


class Result(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="You are 10 bananas tall!")
        label.pack(side="top", fill="both", expand=True)

