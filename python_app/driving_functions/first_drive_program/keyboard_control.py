# Use keyboard control for driving robot
# import serial
# Linux
import keyboard
import serial
import struct
from time import sleep

# Arduino input details:
# struct.pack('>BBBB', speed, direction, turn[0], turn[1])
# int speed: int of range(0, 256), determines current driving speed for forward or reverse
# boolean direction: True drives forward, False drives backward
# int list turn: 0, 1, or 2
# when [0, 1], left turn while driving forward
# [1, 0] right turn while driving forward
# [0, 2] left spin, not driving
# [2, 0] right spin, not driving

# Driving input information
# If up, then positive speed
# If down, then negative speed
# If neither, then 0 speed and 1 direction

# If non-zero speed and left then turn = [0, 1]
# If zero speed and left then turn = [0, 2]
# If non-zero speed and right then turn = [1, 0]
# If zero speed and right then turn = [2, 0]

# Start the serial port to communicate with arduino
data = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Set global arrow variables
left = False
up = False
right = False
down = False

# Storing previous command information to avoid new duplicate commands
previous_turn = [0, 0]
previous_speed = 200

def manageRobot():
    global previous_turn
    global previous_speed
    speed = 200
    turn = [0, 0]

    if up:
        # Positive speed
        pass
    elif down:
        # Negative speed
        speed *= -1
    else:
        # Zero speed
        speed = 0

    if left:
        turn = [0, 1] if speed else [0, 2]
    elif right:
        turn = [1, 0] if speed else [2, 0]
    # print([abs(speed), speed >= 0, turn[0], turn[1]])
    if previous_turn != turn or previous_speed != speed:
        data.write(struct.pack('>BBBB', abs(speed), speed >= 0, turn[0], turn[1]))
        previous_turn = turn
        previous_speed = speed
    

    return True

if __name__ == "__main__":

    while True:
        # Loop to capture key strokes and write date using robot function
        up = keyboard.is_pressed("Up") if not down else False
        down = keyboard.is_pressed("Down") if not up else False
        left = keyboard.is_pressed("Left") if not right else False
        right = keyboard.is_pressed("Right") if not left else False
        # print([up, down, left, right])
        
        manageRobot()
        
        if keyboard.is_pressed("esc"):
            break
        
        sleep(.05)




