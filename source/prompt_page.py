
import tkinter as tk
from page_def import Page
from style import *

class Prompt(Page):
    label = None

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label = tk.Label(
            self, text="Stand on the spot and place your hand on your head!", font=(text_font, 70),bg=background_color, fg=text_color, wraplength=text_wraplength, justify=text_justify)
        self.label.pack(side="top", fill="both", expand=True)
