# This is a fake sensor that returns 100 when the letter 'a' is pressed and a random value between 0 and 100 when any other key is pressed.

import random
import keyboard
from config import *

if SPOOF_SENSOR == False:
    import serial_sensor


class Sensor:
    def get_value(self):
        if SPOOF_SENSOR == False:
            try:
                result = (HEIGHT_OF_SENSOR_MM - serial_sensor.read_me007ys()) / 10
                if result < 0:
                    print("Sensor value below 0")
                    return 0
            except:
                print("Error reading sensor")
                return 0
        else: # Spoof sensor for testing
            # If the 'a' key is pressed, return a value above the threshold
            if keyboard.is_pressed('a'):
                return random.randint(100, 200)
            else:
                return 0
