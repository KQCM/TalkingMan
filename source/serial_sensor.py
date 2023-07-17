import time
import board
import busio
import serial

SERIAL_PORT = "/dev/ttyS0"   # or "COM4" or whatever

serialport = serial.Serial(SERIAL_PORT, 9600)

def read_me007ys(timeout = 1.0):
    ts = time.monotonic()
    buf = bytearray(3)
    idx = 0

    while True:
        if time.monotonic() - ts > timeout:
            raise RuntimeError("Timed out waiting for data")

        c = serialport.read(1)[0]
        if idx == 0 and c == 0xFF:
            buf[0] = c
            idx = idx + 1
        elif 0 < idx < 3:
            buf[idx] = c
            idx = idx + 1
        else:
            chksum = sum(buf) & 0xFF
            if chksum == c:
                return (buf[1] << 8) + buf[2]
            idx = 0
    return None
