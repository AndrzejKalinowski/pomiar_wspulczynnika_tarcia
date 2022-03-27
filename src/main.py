import numpy as np
import serial
import time
import math
import pygame

# pygame stuff
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 600
Y = 600
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)

def main():
    ser = serial.Serial('COM7', 115200)

    x = 0
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
        if delta_distance >= 10 and delta_distance < 50:
            break
        # print(alpha)
        print(delta_distance)

        display_surface.fill(white)
        text = font.render(str(alpha), True, blue, white)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2) 
        display_surface.blit(text, textRect)
        pygame.display.update()

    print("movment detected")
    print("alpha: ", alpha)
    print("delta distance:", delta_distance)
    f = math.tan(math.radians(alpha))
    print("f = ", f)
    display_surface.fill(white)
    text = font.render("f = " + str(f), True, green, white)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2) 
    display_surface.blit(text, textRect)
    pygame.display.update()
    time.sleep(100)
if __name__ == "__main__":
    main()