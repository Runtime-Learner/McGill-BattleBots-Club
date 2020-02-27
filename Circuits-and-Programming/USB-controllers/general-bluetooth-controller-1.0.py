from inputs import devices
from inputs import get_gamepad
from serial.tools import list_ports
import serial
from tkinter import *
from tkinter.ttk import * #used for combobox
import re

import threading
import time
import keyboard  # using module keyboard

window = Tk()
COM_port = ""
connected = False


s = None
#write_timeout = 1


#########################################
#theading functions
#########################################
def thread_keyboardEvent():
    ##flags used to keep track of what keys have been pressed.
    flagB = False
    flagA = False


    ##reduce keyboard sampling rate by only sampling once every 3 times the loop runs
    modulo = 3
    counter = 0
    last = 0
    while True:  # making a loop
        if s is not None and s.is_open:
            if counter == 0:
                try:  # used try so that if user pressed other than the given key errors will not be shown

                    ##detect key presses
                    flagA = keyboard.is_pressed('A')
                    flagB = keyboard.is_pressed('B')
                    time.sleep(0.01)
                except:
                    ##if something goes wrong, send a '0' to the bluetooth module
                    print("eh")
                    sendMsg("!0000")

                ##send out data based on what keys were pressed.
                if flagA:
                    if last != 1:
                        print("a pressed")
                        sendMsg("!9090")
                        last = 1
                elif flagB:
                    if last != 2:
                        print("b pressed")
                        sendMsg("!9191")
                        last = 2
                elif last != 0:
                    sendMsg("!0000")
                    last = 0
            counter = (counter+1)%modulo
        else:
            time.sleep(.25)

#send a message over serial connection if the COM port is open
def sendMsg(message):
    global connected
    if connected:
        s.write(bytes(message,'utf-8'))

#########################################
#events
#########################################

## event triggered when new combobox element is selected
def newPortSelected(event):
    global COM_port
    print("New COM port Selected")
    changeOS()
     
## update the COM_error string
def COM_error(text):
    global COM_port
    lbl_COM_error['text']=text
    disconnect()
    COM_port = ""
    
## get list of serial ports, store them in the COM_combobox
def refresh_COM_list():
    COMlist = []
    for com in list_ports.comports():
        COMlist.append(com)
    combo['values']= COMlist
    combo.set('')
    
    # if length of list is 0, no robot is connected to the computer.
    # notify user, and terminate program
    if len(COMlist) == 0:
        COM_error("No COM port detected...")
    else:
        COM_error("")
        
## change the regex used to get the port name based on the OS selected
def changeOS():
    global COM_port

    disconnect() #disconnect from any port before changing OS
    
    if OsValue.get() == 2: #windows
        x = re.search("COM\d+", str(combo.get()))
        if x != None:
            print(x.group())
            COM_port = x.group()
        else:
            COM_port = ""
    else: #mac OS
        x = re.search("COM\d+", str(combo.get()))
        if x != None:
            print(x.group())
            COM_port = x.group()
        else:
            COM_port = ""
            
def disconnect():
    global COM_port, connected
    if COM_port != "" and connected:
        s.__del__()
        print(s)
        print("disconnected from port " + COM_port)
        lbl_status['text'] = "\nStatus: Disconnected"
    connected = False

def connect():
    print("attempting to connect...")
    global COM_port, connected
    if COM_port != "" and not connected:
        flag = attemptToConnect()
        if flag:
            print("connected to port " + COM_port)
            connected = True
            lbl_status['text'] = "\nStatus: Connected"
        else:
            print("failed to connect to port" + COM_port)
    else:
        print("already connected to a port")

def attemptToConnect():
    global COM_port, s
    try:
        # attempt to connect to that serial port
        s = serial.Serial(COM_port,9600,timeout = 2)
        return True
    except:
        # notify user that we failed to connect to the serial port
        return False        
#########################################
#static labels
#########################################

#COM label
lbl1 = Label(window, text="Select COM port")
lbl1.grid(column=0, row=1)

#connection status
lbl_status = Label(window, text="\nStatus: Disconnected")
lbl_status.grid(column=0, row=3)

#########################################
#dynamic labels
#########################################

#COM error label
lbl_COM_error = Label(window)
lbl_COM_error.grid(column=2, row=2)

#########################################
#Buttons
#########################################
#refresh COM list button
COM_btn = Button(window)
COM_btn['text']="refresh"
COM_btn['command']=refresh_COM_list
COM_btn.grid(column=2, row=1)

#connect to port
COM_btn = Button(window)
COM_btn['text']="connect"
COM_btn['command']=connect
COM_btn.grid(column=1, row=3)

#########################################
#Comboboxes
#########################################

#COM combobox
combo = Combobox(window)
combo['values']= []
combo['state']='readonly'
combo.grid(column=1, row=1)
combo.bind("<<ComboboxSelected>>", newPortSelected) #events with combobox

#########################################
#Radiobuttons
#########################################
OsValue = IntVar() 
OsValue.set(1)

OsOne = Radiobutton(window, text='Windows',
                             variable=OsValue, value=1) 
OsTwo = Radiobutton(window, text='MAC OS',
                             variable=OsValue, value=2) 
OsOne['command']=changeOS
OsTwo['command']=changeOS
OsOne.grid(column=0, row=0)
OsTwo.grid(column=1, row=0)


#initialize list of COM ports before application opens
refresh_COM_list()

#initialize thread
x = threading.Thread(target=thread_keyboardEvent)
x.start()

window.title("Bluetooth-controller-1.0")
window.mainloop()
