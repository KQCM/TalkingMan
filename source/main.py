import tkinter as tk
from page_def import Page
from idle_page import Idle
from result_page import Result
from prompt_page import Prompt
from sensor import Sensor
import time
import numpy as np

from config import *

# States
IDLE = 0
PROMPT = 1
DISPLAY = 2


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.sensor = Sensor()
        self.state = IDLE

        self.idle_screen = Idle(self)
        self.prompt_screen = Prompt(self)
        self.result_screen = Result(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.idle_screen.place(in_=container, x=0, y=0,
                               relwidth=1, relheight=1)
        self.prompt_screen.place(
            in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.result_screen.place(
            in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.run()

    def run(self):
        if self.state == IDLE:
            self.do_idle()

        elif self.state == PROMPT:
            self.do_prompt()

        elif self.state == DISPLAY:
            self.do_display()

    def do_idle(self):
        if self.sensor.get_value() > SENSOR_DETECT_THRESHOLD:
            self.state = PROMPT
            self.run()
        else:
            self.idle_screen.show()
            self.after(DETECT_GUEST_MS, lambda: self.do_idle())

    def _determine_result(self, values):
        self.guest_height = np.median(values)

        # If the median value is above the threshold, then the guest is still
        if self.guest_height > SENSOR_DETECT_THRESHOLD:
            self.state = DISPLAY
            self.run()
        else:
            self.guest_height = 0
            self.state = IDLE
            self.run()

    def do_prompt(self):
        self.prompt_screen.show()

        values = []
        for i in range(0, STILL_TIME_MS, DETECT_GUEST_MS):
            self.after(i, lambda: values.append(self.sensor.get_value()))

        self.after(STILL_TIME_MS, lambda: self._determine_result(values))

    def _log_height(self, height):
        with open("../data/guest_heights.txt", "a+") as f:
            # Write the timestamp and height
            f.write(str(time.strftime("%m/%d/%Y-%H:%M")) +
                    "," + str(height) + "\n")

        # Update the idle screen
        self.idle_screen.add_data(height)

    def do_display(self):
        if (not self.guest_height):
            self.state = IDLE
            self.run()
            return

        self.result_screen.set_height(self.guest_height)
        self.result_screen.show()
        self._log_height(self.guest_height)
        tk.Tk.update(self)
        self.result_screen.read_height(self.guest_height)

        # Set the state back to idle after a few seconds
        self.state = IDLE
        self.after(DISPLAY_RESULT_TIME_MS, lambda: self.idle_screen.show())
        self.after(DISPLAY_RESULT_TIME_MS + FORCE_WAIT_TIME, lambda: self.run())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Talking Man")
    root.attributes("-fullscreen", True)
    root.wm_geometry("400x400")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
