import re
from tkinter import *
from tkinter.ttk import * #used for combobox


################
#events
###############
def tb1_enter():
    txt2.focus()
def tb2_enter():
    x = re.search("\S+", txt1.get())
    y = re.search("\S+", txt2.get())
    if x != None and y != None: 
        Lb1.insert(END, x.group() + " => " + y.group())
    txt1.delete(first=0, last = len(txt1.get()))
    txt2.delete(first=0, last = len(txt2.get()))
    txt1.focus()
        
def deleteFromCommands():
    Lb1.delete(ANCHOR)


def on_closing():
    print("closing")
    for string in Lb1.get(0, END):
        x = re.search("^\S+", string)
        y = re.search("\S+$", string)
        if x != None:
            print(x.group() + " , "  + y.group())
            COM_port = x.group()
##        print(str)
    window2.destroy()
    
window2 = Tk()


#row 0
lbl = Label(window2, text="Input sequence") 
lbl.grid(column=0, row=0)

lbl2 = Label(window2, text="Command")
lbl2.grid(column=1, row=0)

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
lbl = Label(window2, text="----------------") 
lbl.grid(column=0, row=2)
lbl = Label(window2, text="----------------") 
lbl.grid(column=1, row=2)

#row 3
lbl = Label(window2, text="commands list") 
lbl.grid(column=0, row=3)

#row 4
Lb1 = Listbox(window2) #list of commands
Lb1['height'] = 10
Lb1.grid(column=0, row=4)

COM_btn = Button(window2) #delete from Commands list
COM_btn['text']="delete"
COM_btn['command']=deleteFromCommands
COM_btn.grid(column=1, row=4)


window2.title("commands profile")
window2.protocol("WM_DELETE_window2", on_closing)
window2.mainloop()
