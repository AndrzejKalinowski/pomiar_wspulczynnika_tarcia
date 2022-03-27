import numpy as np
import serial
import time
import math
ser = serial.Serial('COM7', 115200)
if __name__ == "__main__":
    x = 0
    y = 0
    z = 0
    distance = 0
    print("hello")
    time.sleep(2)
    print("starting mesurment")
    while True:
        prev_distance = distance
        # reading data from the arduino
        line = ser.readline()
        # interpreting data form arduion
        if line[0] == 88:
            x = float(line[2:6])
        elif line[0] == 90:
            z = float(line[2:6])
        elif line[0] == 68:
            try:
                distance = float(line[2:6])
            except ValueError:
                distance = -1
        
        #calculating the angle
        try:
            alpha = 90 - math.degrees(np.arctan(z/x))
        except ZeroDivisionError:
            alpha = 0
        
        delta_distance = distance - prev_distance
        if delta_distance >= 5 and delta_distance < 50:
            pass
        # print(alpha)
        print(delta_distance)