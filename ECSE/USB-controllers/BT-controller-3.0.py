from inputs import get_gamepad
import serial
import numpy as np
from math import sin, cos, pi, radians, sqrt


def transform(x, y):
    abs_dist = sqrt(x*x + y*y)
    if abs_dist > 1:
        abs_dist = 1
    #print(abs_dist)
    wheelRatio = abs(x)
    newL = abs_dist
    newR = abs_dist - wheelRatio*2
    if x < 0:
        tmp = newL
        newL = newR
        newR = tmp
    if y < 0:
        newL = -newL
        newR = - newR

    newR = (int)(newR*9)
    newL = (int)(newL*9)
    return (newR, newL)



s = serial.Serial("COM9",9600,timeout = 2)
X = "00"
Y = "00"
evX = False
evY = False
eventZ = False
evZ = 0
modulo = 0
lastX = 0
lastY = 0


while 1:
    events = get_gamepad()
    for event in events:
        if event.ev_type == "Absolute":
            tmpX = lastX
            tmpY = lastY
            if event.code == "ABS_X":
                evX = True
                tmpX = (event.state/32770)
                
            if event.code == "ABS_Y":
                evY = True
                tmpY = (event.state/32770)

            if event.code == "ABS_Z":
                evZ = (int)(event.state)
                eventZ = True
                print("evZ\n")

            
            if (int)(tmpX*25) == (int)(lastX*25):
                evX = False
            else:
                lastX = tmpX
            if (int)(tmpY*25) == (int)(lastY*25):
                evY = False
            else:
                lastY = tmpY

            (tmpX, tmpY) = transform(tmpX, tmpY)


            if evZ > 0:
                if tmpX != 0:
                    tmpX = (int)(tmpX/2)
                if tmpY != 0:
                    tmpY = (int)(tmpY/2)
            
            #store the value of X inside a string
        
            if tmpX < 0:
                X = "1"
                tmpX = tmpX * -1
            else:
                X = "0"
            X = ((str)(tmpX % 10)) + X
                    
            #store the value of Y inside a string
            
            if tmpY < 0:
                Y = "1"
                tmpY = tmpY * -1
            else:
                Y = "0"
            Y = ((str)(tmpY % 10)) + Y
       
        #only send one message out of 2 to decrease lag
        if evX or evY or eventZ:
            evY = False
            evX = False
            eventZ = False
            print(X +"\t"+ Y) #L + R motors
            s.write(bytes("!" + X + Y + ".",'utf-8'))
