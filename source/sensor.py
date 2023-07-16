# This is a fake sensor that returns 100 when the letter 'a' is pressed and a random value between 0 and 100 when any other key is pressed.

import random
import keyboard

class Sensor:
    def get_value(self):
        if keyboard.is_pressed('a'):
            return random.randint(100, 120)
        else:
            return 0

        