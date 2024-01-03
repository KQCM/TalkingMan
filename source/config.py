# How long to wait for a guest to stand still before measuring their height, in milliseconds
# The final height is the median of all the values read during this time
STILL_TIME_MS = 3000

# The threshold for the sensor to detect a guest, in cm
SENSOR_DETECT_THRESHOLD = 45

# How often to check the sensor for a guest, in milliseconds
DETECT_GUEST_MS = 300

# How many bins to use for the histogram
BIN_COUNT = 15

# How long to display the result screen for, in milliseconds
DISPLAY_RESULT_TIME_MS = 8000

# How long to wait after displaying the idle screen before checking for a guest again, in milliseconds
FORCE_WAIT_TIME = 1000

# The operating system that the program is running on
OS = "Linux" # "Windows" or "Linux"

# Whether or not to spoof the sensor for testing
SPOOF_SENSOR = False

# The height of the sensor from the ground, in cm
HEIGHT_OF_SENSOR_CM = 259
