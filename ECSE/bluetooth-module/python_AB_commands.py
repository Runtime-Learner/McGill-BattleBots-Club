##This is a simple program used to connect to a bluetooth module
##from a serial port. It sends a '1' when the letter A is pressed and a '0' when
##the letter B is pressed.


import keyboard  # using module keyboard
import serial
import time
from serial.tools import list_ports
import re #regex library


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
        x = re.search("COM\d+", str(list[g]))
        s = serial.Serial(x.group(),9600,timeout = 2)
        serialFlag = True
    except:
        # notify user that we failed to connect to the serial port
        print("failed to connect to serial port \"" + x.group() + "\"")
        serialFlag = False


#####################################################################
## This is the part of the code that actually detects key presses and send out
## signals to the bluetooth module.


##flags used to keep track of what keys have been pressed.
flagB = False
flagA = False


##reduce keyboard sampling rate by only sampling once every 3 times the loop runs
modulo = 3
counter = 0

while True:  # making a loop
        if counter == 0:
            try:  # used try so that if user pressed other than the given key errors will not be shown

                ##detect key presses
                flagA = keyboard.is_pressed('A')
                flagB = keyboard.is_pressed('B')
                time.sleep(0.01)
            except:
                ##if something goes wrong, send a '0' to the bluetooth module
                s.write(bytes("0",'utf-8'))
                
        counter = (counter+1)%modulo


        ##send out data based on what keys were pressed.
        if flagA:
            print("a pressed")
            s.write(bytes("1",'utf-8'))
            flagA = False
        
        if flagB:
            print("b pressed")
            s.write(bytes("0",'utf-8'))
            flagB = False
