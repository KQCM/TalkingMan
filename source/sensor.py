import random
import keyboard
import board
import time
from config import *
import adafruit_vl53l1x

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

vl53 = adafruit_vl53l1x.VL53L1X(i2c)

# OPTIONAL: can set non-default values
vl53.distance_mode = 2
vl53.timing_budget = 200


class Sensor:
    def start_sensor(self):
        vl53.start_ranging()
    def get_value(self):
        if SPOOF_SENSOR == False:
            try:
                result = (HEIGHT_OF_SENSOR_CM - vl53.distance)
            except:
                print("Error reading sensor")
                return 0
            else:
                if result == None:
                    return 0
                else:
                    if result < 0:
                        print("Sensor value below 0")
                        return 0
                    else:
                        return result
            vl53.clear_interrupt()
        else: # Spoof sensor for testing
            # If the 'a' key is pressed, return a value above the threshold
            if keyboard.is_pressed('a'):
                return random.randint(100, 200)
            else:
                return 0
