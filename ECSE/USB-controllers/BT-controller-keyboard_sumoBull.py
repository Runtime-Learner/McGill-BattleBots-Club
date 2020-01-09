import keyboard  # using module keyboard
import serial
import time

flagW = False
flagA = False
flagS = False
flagD = False
turnedOff = False
last = -1
g = input("Enter serial port for sumoBull : ") 
s = serial.Serial(g,9600,timeout = 2)
#s.write(bytes("!9090.",'utf-8'))

modulo = 1
counter = 0

while True:  # making a loop
    if counter == 0:
        try:  # used try so that if user pressed other than the given key error will not be shown
            flagW = keyboard.is_pressed('w')
            flagA = keyboard.is_pressed('a')
            flagS = keyboard.is_pressed('s')
            flagD = keyboard.is_pressed('d')
        except:
            if last != 0:
                s.write(bytes("!0000.",'utf-8'))
            last = 0
            break
    time.sleep(0.001)
    counter = (counter+1)%modulo
    dY = 0
    dX = 0
    if not (flagW and flagS):
        if flagW:
            dY = 1
        if flagS:
            dY = -1
    if not (flagA and flagD):
        if flagD:
            dX = 1
        if flagA:
            dX = -1

    if dY == 0 and dX == 0:
        if last != 0:
            print("idle")
            s.write(bytes("!0000",'utf-8'))
        last = 0
    elif dX == 0:
        if dY == 1:
            if last != 1:
                print("up")
                s.write(bytes("!9090",'utf-8'))
            last = 1
        if dY == -1:
            if last != 2:
                print("down")
                s.write(bytes("!9191",'utf-8'))
            last = 2
    elif dY == 0:
        if dX == -1:
            if last != 3:
                print("right")
                s.write(bytes("!9190",'utf-8'))
            last = 3
        if dX == 1:
            if last != 4:
                print("left")
                s.write(bytes("!9091",'utf-8'))
            last = 4

    
        
        
