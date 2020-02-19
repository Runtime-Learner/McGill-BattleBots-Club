from inputs import get_gamepad
import serial


#gets the x and y values from the controller joystick
#values range between [-1,1]
def transform(x, y):
    abs_dist = sqrt(x*x + y*y)
    if abs_dist > 1:
        abs_dist = 1
        
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




#connect to the serial port 9 to send data to the blutooth module
#you probably have to change this
s = serial.Serial("COM9",9600,timeout = 2)

#text encoding of commands (this is what we will be sending over BT)
X = "00"
Y = "00"

#flags used to detect changes in player input
evX = False
evY = False
eventZ = False
evZ = 0
modulo = 0
lastX = 0
lastY = 0


#infinite loop.
while 1:

    #get events from the gamepad
    events = get_gamepad()
    for event in events:
        #parse through the events by type (each controller key has a different type)
        if event.ev_type == "Absolute": 
            tmpX = lastX
            tmpY = lastY
            if event.code == "ABS_X":
                evX = True
                tmpX = (event.state/32770) #get joystick X input. Normalize it
                
            if event.code == "ABS_Y":
                evY = True
                tmpY = (event.state/32770) #get joystick Y input. Normalize it

            if event.code == "ABS_Z":
                evZ = (int)(event.state)
                eventZ = True
                print("evZ\n")


            #if X coordinate hasn't changed, turn off flag
            if (int)(tmpX*25) == (int)(lastX*25):
                evX = False
            else:
                lastX = tmpX
                
            #if Y coordinate hasn't changed, turn off flag
            if (int)(tmpY*25) == (int)(lastY*25):
                evY = False
            else:
                lastY = tmpY

            #take normalized XY coordinates and transform into bot commands
            (tmpX, tmpY) = transform(tmpX, tmpY)


            #dw about this.
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
       
        #only send a message if a new event has been registered (a flag has been raised)
        if evX or evY or eventZ:
            evY = False
            evX = False
            eventZ = False
            print(X +"\t"+ Y) #L + R motors
            
            string = "!" + X + Y + "."
            s.write(bytes(string,'utf-8'))
