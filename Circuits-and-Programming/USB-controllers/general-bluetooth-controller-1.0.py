from inputs import devices
from inputs import get_gamepad
from serial.tools import list_ports
from tkinter import *
from tkinter.ttk import * #used for combobox
import re

window = Tk()
COM_port = ""
connected = False

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
        print("disconnected from port " + COM_port)
        lbl_status['text'] = "\nStatus: Disconnected"
    connected = False

def connect():
    print("attempting to connect...")
    global COM_port, connected
    if COM_port != "" and not connected:
        print("connected to port " + COM_port)
        connected = True
        lbl_status['text'] = "\nStatus: Connected"
        
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

window.title("Bluetooth-controller-1.0")
window.mainloop()
