from inputs import devices
from inputs import get_gamepad
import tkinter as tk

for device in devices:
    print(device)

#while 1:
    #events = get_gamepad()
    #for event in events:
    #    print(event.ev_type, event.code, event.state)


main = tk.Tk() 
main.mainloop() 