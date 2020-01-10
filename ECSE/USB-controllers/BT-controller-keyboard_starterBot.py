import keyboard  # using module keyboard
import serial
import time
from serial.tools import list_ports

flagW = False
flagA = False
flagS = False
flagD = False
turnedOff = False
last = -1



# get list of serial ports, store them in a list
list = []
counter = 0
for com in list_ports.comports():
	list.append(com)

for x in range(0, len(list)):
        print(str(x) + ")\t" + str(list[x]))

# if length of list is 0, no robot is connected to the computer.
# notify user, and terminate program
if len(list) == 0:
    print("no serial ports detected....please turn on your devices and try again")
    input("\n\nPress enter to continue\n\n")
    exit()


serialFlag = False
while serialFlag == False:
    #ask for user input. Repeat if user input is invalid
    flag = False
    while flag == False:
        g = input("Enter serial port number: ")
        
        try:
            # ignore all occurences of key presses that could be caused by
            # controller presses.
            g = g.replace("w", "")
            g = g.replace("a", "")
            g = g.replace("s", "")
            g = g.replace("d", "")
            g = g.replace("t", "")
            g = g.replace("f", "")
            g = g.replace("g", "")
            g = g.replace("h", "")

            # convert parsed input to integer
            g = int(g)
            flag = True

            #insure that the user input is a valid index in the list
            if g < 0 or g > (len(list)-1):
                flag = False
                print("Input out of bounds. Choose a port between 0 and " + str((len(list)-1)))
        except:
            print("input must be a number")
            flag = False
            
    try:
        # attempt to connect to that serial port
        s = serial.Serial(list[g],9600,timeout = 2)
        serialFlag = True
    except:
        # notify user that we failed to connect to the serial port
        print("failed to connect to serial port \"" + list[g] + "\"")
        serialFlag = False

while True:  # making a loop

    try:  # used try so that if user pressed other than the given key error will not be shown
        flagW = keyboard.is_pressed('t')
        flagA = keyboard.is_pressed('f')
        flagS = keyboard.is_pressed('g')
        flagD = keyboard.is_pressed('h')
    except:
        if last != 0:
            s.write(bytes("!0000",'utf-8'))
        last = 0
        break
        
    time.sleep(0.001)
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
        if dX == 1:
            if last != 3:
                print("right")
                s.write(bytes("!9190",'utf-8'))
            last = 3
        if dX == -1:
            if last != 4:
                print("left")
                s.write(bytes("!9091",'utf-8'))
            last = 4

    
        
        
