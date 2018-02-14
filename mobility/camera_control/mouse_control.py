# import required libraries
import serial
import struct
from vpython import arrow, label, rate, vector
import numpy as np
import pyHook
import pythoncom
import time
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

# Mouse support
screen_size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
hm = pyHook.HookManager()

# Start the serial port to communicate with arduino
data = serial.Serial('com3', 9600, timeout=1)

# first we create the arrow to show current position of the servo
measuringArrow = arrow(pos=vector(0, -10, 0), axis=vector(-10, 3, 0), shaftwidth=0.4, headwidth=0.6)
angleLabel = label(text='LED Status', pos=vector(0, 5, 0), height=15, box=False)
angle0 = label(text='Off', pos=vector(-10, -10, 0), height=15, box=False)
angle180 = label(text='On', pos=vector(10, -10, 0), height=15, box=False)


# Turn on
def turn_on(event):
    data.write(struct.pack('>BBB', 2, 0, 0))
    measuringArrow.axis = vector(10, 3, 0)
    myLabel = 'LED is: On'
    angleLabel.text = myLabel
    return True


# Turn off
def turn_off(event):
    data.write(struct.pack('>BBB', 1, 0, 0))
    measuringArrow.axis = vector(-10, 3, 0)
    myLabel = 'LED is: Off'
    angleLabel.text = myLabel
    return True


def set_servo(event):
    x = screen_size[0]
    x_mouse_pos = event.Position[0]
    x_servo_pos = int((x_mouse_pos / x) * 180)

    y = screen_size[1]
    y_mouse_pos = event.Position[1]
    y_servo_pos = int((y_mouse_pos / y) * 180) + 100  # Offset by 100 degrees

    # Print servo commands
    print((x_servo_pos, y_servo_pos))

    data.write(struct.pack('>BBB', 0, x_servo_pos, y_servo_pos))
    return True

hm.MouseLeftDown = turn_on
hm.MouseLeftUp = turn_off
hm.MouseMove = set_servo

hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()
