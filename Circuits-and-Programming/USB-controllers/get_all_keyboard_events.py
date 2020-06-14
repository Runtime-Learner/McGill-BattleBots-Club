from inputs import get_key, devices
import serial
import re
from tkinter import *
from tkinter.ttk import * #used for combobox
import threading


end = True


def hi():
    global end
    last = ""
    #infinite loop.
    while not end:
        #get events from the gamepad
        events = get_key()

        if events:
            for event in events:
                x = re.search("KEY_\S", str(event.code))
                if x != None and last != x.group():
                    #print(x.group())
                    lbl['text']=x.group()
                    last = x.group()
    return

def main():
    print("done")

def buttonEvent():
    #initialize thread
    global end
    end = False
    print("start")
    x = threading.Thread(target=hi)
    x.start()
    
def buttonEvent2():
    global end
    end = True
    print("stop")

                
if __name__ == "__main__":
    
    window = Tk()
    window.title("derp")

    #LABELS
    lbl = Label(window, text="Hi") #can create label like this
    lbl.grid(column=0, row=0)

    #BUTTONS
    btn = Button(window)
    btn['text']="keyCall"
    btn['command']=buttonEvent
    btn.grid(column=1, row=0)

    btn = Button(window)
    btn['text']="endKeyCall"
    btn['command']=buttonEvent2
    btn.grid(column=2, row=0)
    
    window.mainloop()
    main()
    
    
