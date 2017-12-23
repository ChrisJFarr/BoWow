# Use keyboard control for driving robot
# import serial
import pyHook
import pythoncom
import serial
import struct

# Start the serial port to communicate with arduino
data = serial.Serial('com3', 9600, timeout=1)

# todo Turns should add a bit to one side and remove a bit from the other
# todo Speed should be a constant level
# todo Robot should stop when no buttons are pressed
# todo Fix the turning inversion while driving

left = False
up = False
right = False
down = False


def logPress(event):
    global left
    global up
    global right
    global down

    if event.Key == "Left":
        left = True
        right = False
    elif event.Key == "Up":
        up = True
        down = False
    elif event.Key == "Right":
        right = True
        left = False
    elif event.Key == "Down":
        down = True
        up = False

    return manageRobot()


def logRelease(event):
    global left
    global up
    global right
    global down

    if event.Key == "Left":
        left = False
    elif event.Key == "Up":
        up = False
    elif event.Key == "Right":
        right = False
    elif event.Key == "Down":
        down = False

    return manageRobot()


def manageRobot():
    global left
    global up
    global right
    global down
    speed = 200
    turn = [0, 0]

    if up:
        speed *= 1
    elif down:
        speed *= -1
    else:
        speed *= 0

    if left:
        turn = [0, 1] if speed else [0, 2]
    elif right:
        turn = [1, 0] if speed else [2, 0]
    # print([abs(speed), speed >= 0, turn[0], turn[1]])
    data.write(struct.pack('>BBBB', abs(speed), speed >= 0, turn[0], turn[1]))

    return True

# If up, then positive speed
# If down, then negative speed
# If neither, then 0 speed and 1 direction

# If non-zero speed and left then turn = [0, 1]
# If zero speed and left then turn = [0, 2]
# If non-zero speed and right then turn = [1, 0]
# If zero speed and right then turn = [2, 0]

# create a hook manager
hm = pyHook.HookManager()


# watch for all mouse events
hm.KeyDown = logPress
hm.KeyUp = logRelease
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
hm.UnhookKeyboard()
