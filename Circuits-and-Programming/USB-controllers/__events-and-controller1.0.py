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



#########
#GLOBAL VARIABLES
#########
commandsList = []
defaultCommand = "0"

#########
#GLOBAL FUNCTIONS
#########
def getBool(myList): 
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return bool(result)




####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
################
#events
###############
def tb1_enter():
    txt2.focus()
    
def tb2_enter():
    x = re.search("\S", txt1.get())
    y = re.search("\S+", txt2.get())
    if x != None and y != None: 
        Lb1.insert(END, x.group() + " => " + y.group())
    txt1.delete(first=0, last = len(txt1.get()))
    txt2.delete(first=0, last = len(txt2.get()))
    txt1.focus()
        
def deleteFromCommands():
    Lb1.delete(ANCHOR)

def initializeCommandsList():
    global commandsList
    for item in commandsList:
        (x, y) = item
        Lb1.insert(END, x + " => " + y)
    Lb1.insert(END, "~ => " + defaultCommand)
        
def on_closingProfiler():
    global commandsList, s, defaultCommand
    print("closing")
    commandsList = []
    hasDefaultCommand = False
    for string in Lb1.get(0, END):
        x = re.search("^\S+", string)
        y = re.search("\S+$", string)
        if x != None:
            print(x.group() + " , "  + y.group())
            if x.group() == "~":
                hasDefaultCommand = True
                defaultCommand = y.group()
            else:
                commandsList.append((x.group(), y.group()))

    if hasDefaultCommand:
        window2.destroy()
    else:
        print("need default command (~)!")



###################
#creation of event creator
###################
window2 = None
#row1
txt1 = None

txt2 = None

#row 4
Lb1 = None

COMS_btn = None

def create_profile_window():
    global window2, txt1, txt2, Lb1, COMS_btn, s

    disconnect()
    
    window2 = Toplevel()


    #row 0
    lbl5 = Label(window2, text="Keyboard key") 
    lbl5.grid(column=0, row=0)

    lbl5 = Label(window2, text="Command to send")
    lbl5.grid(column=1, row=0)

    #row1
    txt1 = Entry(window2,width=10)
    txt1.grid(column=0, row = 1)
    txt1.get() #gets the info inside the textbox
    txt1.focus() #set focus to entry widget
    txt1.bind("<Return>", (lambda event:tb1_enter() ))

    txt2 = Entry(window2,width=10)
    txt2.grid(column=1, row = 1)
    txt2.bind("<Return>", (lambda event:tb2_enter()))

    #row2 ###filler
    lbl5 = Label(window2, text="----------------") 
    lbl5.grid(column=0, row=2)
    lbl5 = Label(window2, text="----------------") 
    lbl5.grid(column=1, row=2)

    #row 3
    lbl5 = Label(window2, text="commands list") 
    lbl5.grid(column=0, row=3)

    #row 4
    Lb1 = Listbox(window2) #list of commands
    Lb1['height'] = 10
    Lb1.grid(column=0, row=4)
    initializeCommandsList()

    COMS_btn = Button(window2) #delete from Commands list
    COMS_btn['text']="delete"
    COMS_btn['command']=deleteFromCommands
    COMS_btn.grid(column=1, row=4)


    window2.title("commands profile")
    window2.protocol("WM_DELETE_WINDOW", on_closingProfiler)
    window2.grab_set()
    window2.mainloop()
    
    
    
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

window = Tk()
COM_port = ""
connected = False


s = None
#write_timeout = 1

#########################################
#theading functions
#########################################
def thread_keyboardEvent():
    print("starting keyboardsLoop")
    global commandsList, s, defaultCommand

##flags used to keep track of what keys have been pressed.
    lastCommand = -2 #does not map to any command
    flagList = []
    for i in range(0, len(commandsList) + 1):
        flagList.append(False)


    ##reduce keyboard sampling rate by only sampling once every 3 times the loop runs
    modulo = 3
    counter = 0
    last = 0
    while True:  # making a loop
        if s is not None and s.is_open:
            if counter == 0:
                try:  # used try so that if user pressed other than the given key errors will not be shown

                    ##detect key presses
                    for i in range(0, len(commandsList)):
                        flagList[i] = keyboard.is_pressed(commandsList[i][0])
                    time.sleep(0.01)
                except:
                    ##if something goes wrong, send a '0' to the bluetooth module
                    print("failed to read keyboard")
                    if lastCommand != -1:
                        sendMsg(defaultCommand)
                        lastCommand = -1 #maps to the default command

                ##send out data based on what keys were pressed.
                globalFlag = False
                for i in range(0, len(commandsList)):
                    if flagList[i]:
                        if lastCommand != i:
                            sendMsg(commandsList[i][1])
                            lastCommand = i
                        globalFlag = True
                if not globalFlag and lastCommand != -1:
                    sendMsg(defaultCommand)
                    lastCommand = -1
            counter = (counter+1)%modulo
        else:
            time.sleep(.25)
            print("ending keyboards loop")
            return

#send a message over serial connection if the COM port is open
def sendMsg(message):
    global connected
    if connected:
        s.write(bytes(message,'utf-8'))
    print(message)

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
    global COM_port, connected, s, defaultCommand
    if COM_port != "" and connected:
        sendMsg(defaultCommand)
        s.__del__()
        print(s)
        print("disconnected from port " + COM_port)
        lbl_status['text'] = "\nStatus: Disconnected"
    connected = False

def connect():
    print("attempting to connect...")
    global COM_port, connected, s
    if COM_port != "" and not connected:
        flag = attemptToConnect()
        if flag:
            print("connected to port " + COM_port)
            connected = True
            lbl_status['text'] = "\nStatus: Connected"
        else:
            print("failed to connect to port" + COM_port)
    else:
        print("failed to connect to port")

def attemptToConnect():
    global COM_port, s
    try:
        # attempt to connect to that serial port
        s = serial.Serial(COM_port,9600,timeout = 2)
        #initialize thread
        x = threading.Thread(target=thread_keyboardEvent)
        x.start()
        return True
    except:
        # notify user that we failed to connect to the serial port
        return False


def openProfiler():
    create_profile_window()

def on_closingMain():
    global commandsList, s
    disconnect()
    window.destroy()
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

#alter commands list
COM_btn = Button(window)
COM_btn['text']="change Commands list"
COM_btn['command']= openProfiler
COM_btn.grid(column=1, row=4)

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

window.title("Bluetooth-controller-1.0")
window.protocol("WM_DELETE_WINDOW", on_closingMain)
window.mainloop()
