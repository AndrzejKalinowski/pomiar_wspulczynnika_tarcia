import numpy as np
import serial
import time
ser = serial.Serial('COM7', 115200)
if __name__ == "__main__":
    print("hello")
    time.sleep(2)
    print("starting mesurment")
    while True:
        line = ser.readline()
        if line[0] == 68:
            print(line)