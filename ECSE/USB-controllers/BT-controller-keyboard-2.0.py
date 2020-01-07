from pynput.keyboard import Key, Listener
import serial


s = serial.Serial("COM8",9600,timeout = 2)


def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == 'w':
        s.write(bytes("!9090.",'utf-8'))
    #else:
     #   s.write(bytes("!0000.",'utf-8'))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


