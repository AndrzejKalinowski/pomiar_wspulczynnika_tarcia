import numpy as np
import serial
import time
import math
ser = serial.Serial('COM7', 115200)
if __name__ == "__main__":
    x = 0
    y = 0
    z = 0
    print("hello")
    time.sleep(2)
    print("starting mesurment")
    while True:
        line = ser.readline()
        # print(line)
        if line[0] == 88:
            # print(line)
            x = float(line[2:6])
        elif line[0] == 89:
            y = float(line[2:6])
        elif line[0] == 90:
            z = float(line[2:6])
        elif line[0] == 44:
            distance = float(line[2:6])
        
        # print(x, y, z)
        try:
            alpha = 90 - math.degrees(np.arctan(z/x))
        except ZeroDivisionError:
            alpha = 0
        print(alpha)