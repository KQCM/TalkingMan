# TalkingMan
Measurment Station for Museums

This project reads the height of a patron, displays it on a screen in both centimeters and a rotating selection of other units, then reads it out loud with a voice synthesizer. After reading outloud it adds the height reading to a database and displays a chart of all heights recorded.

Hardware:
Raspberry Pi 4
HDMI screen with speakers
Adafruit VL53L1X ToF distance sensor
Sparkfun I2C hat for Raspberry Pi
Adafruit LTC4311 I2C Extender (optional depending on distance from sensor to computer)

Dependencies:
Adafruit CircuitPython
Adafruit VL53L1X driver
Tkinter
MatPlotLib
Festival TTS
